import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

// news-image-20261124 v3-local: the front page is painted by
// draw24-v3.py (PIL, run at build time) and shipped as entry.png.
// This entrypoint only carries that file to the grader and checks
// it is whole first: right magic, right size, under the byte cap.
// It reads nothing else, touches no network, and writes the same
// bytes on every run, whatever the working directory is.
const folder = fileURLToPath(new URL(".", import.meta.url));
const sourcePath = join(folder, "entry.png");
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? join(folder, "out");

const MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

function fail(msg: string): never {
  throw new Error(msg);
}

function sha256(bytes: Buffer): string {
  return createHash("sha256").update(bytes).digest("hex");
}

function checkPng(bytes: Buffer): void {
  if (bytes.length < 33) fail("entry.png is too short to be a PNG");
  if (!bytes.subarray(0, 8).equals(MAGIC)) {
    fail("entry.png does not start with the PNG magic bytes");
  }
  const width = bytes.readUInt32BE(16);
  const height = bytes.readUInt32BE(20);
  if (width !== 1024 || height !== 1024) {
    fail(`entry.png is ${width}x${height}, want 1024x1024`);
  }
  const colourType = bytes[25];
  if (colourType !== 2 && colourType !== 6) {
    fail(`entry.png colour type ${colourType}, want 2 or 6`);
  }
  if (bytes.length > 1024 * 1024) {
    fail(`entry.png is ${bytes.length} bytes, over the 1 MiB cap`);
  }
}

if (!existsSync(sourcePath)) {
  fail("entry.png is missing beside main.ts — run draw24-v3.py first");
}
const png = readFileSync(sourcePath);
checkPng(png);

mkdirSync(targetDir, { recursive: true });
const destPath = join(targetDir, "entry.png");
writeFileSync(destPath, png);

const back = readFileSync(destPath);
if (back.length !== png.length) fail("entry.png copy came up short");
if (sha256(back) !== sha256(png)) {
  fail("entry.png copy hash does not match the source");
}
console.log(
  `entry.png OK (${png.length} bytes, sha256 ${sha256(png)}) -> ${destPath}`,
);
