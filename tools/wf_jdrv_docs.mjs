export const meta = {
  name: 'elfbot-jdrv-deepdocs',
  description: 'Deep-document the 457 undocumented .jdrv bot functions of elfbot.dll',
  phases: [{ title: 'Document', detail: 'one agent per chunk: decompiled C -> name + specific purpose' }],
}

const CHUNKS = 32
const CDIR = '/tmp/claude-1000/-home-kizudev-Documents-Repos-magebot-re/9b8c3669-5386-483d-bbab-ee0854da4916/scratchpad/elfbot_chunks'
const RDIR = '/tmp/claude-1000/-home-kizudev-Documents-Repos-magebot-re/9b8c3669-5386-483d-bbab-ee0854da4916/scratchpad/elfbot_results'
const REPO = '/home/kizudev/Documents/Repos/elfbot_re'

const GUIDE = `You are reverse-engineering **ElfBot NG 8.60**, a memory-injection bot for the
Tibia 8.60 client (a Windows DLL, elfbot.dll, imagebase 0x10000000). The \`.jdrv\`
section is the BOT LOGIC (not library code). Your job: for each function in your
assigned chunk, read its decompiled pseudo-C and write a SPECIFIC, grounded
one-to-two-sentence purpose — what the function is FOR — plus a descriptive name.

Repo for cross-reference (read as needed): ${REPO}/docs — 08-client-hooks-engine,
09-packet-proxy, 10-feature-subsystems, 11-ciroscript-engine, 12-script-crypto-
compression, 05-ui-init-framework. The bot's subsystems: client memory hooks,
embedded packet proxy / NavNet, CiroScript interpreter (cmd_* handlers), cavebot
walker, targeting/AutoAim, healer, hotkeys, HUD, looter, script crypto.

QUALITY BAR (match these real examples):
- "packetOpcodeHasCoordFlag": "Tests bit 0x08 of a per-map-tile record byte
  (76-byte stride table at *0x785db4) to decide if an item carries an extra
  coord/stack byte."
- "startNavServerThread": "Stores config arg in g_10042000 and, if mode==1,
  spawns the NavNet server worker thread sub_10002041 via CreateThread."
Ground every purpose in the actual code: name the globals it touches, the APIs it
calls, the constants/opcodes it tests, the helper subs it calls, the strings it
references. NO generic filler ("helper function", "does processing", "library/
support"). If a function is a thin wrapper/thunk, say what it wraps. If you truly
cannot tell, give the best structural description AND set confidence:"low".

NAMING: propose a camelCase descriptive name (e.g. \`readCreatureHpBar\`,
\`cmd_gotoLabel\`, \`encodeMovePacket\`). If existing_name is already set and good,
reuse it. Names must be valid C identifiers, unique-ish, no spaces.`

const SCHEMA = {
  type: 'object',
  required: ['entries'],
  properties: {
    entries: {
      type: 'array',
      items: {
        type: 'object',
        required: ['addr', 'name', 'purpose', 'confidence'],
        properties: {
          addr: { type: 'string', description: 'function address like 0x1000xxxx (copy from input)' },
          name: { type: 'string', description: 'camelCase descriptive C identifier' },
          purpose: { type: 'string', description: 'specific 1-2 sentence purpose grounded in the code' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
        },
      },
    },
  },
}

phase('Document')
const idx = Array.from({ length: CHUNKS }, (_, i) => i)
const results = await parallel(idx.map(i => () => {
  const cf = `${CDIR}/chunk_${String(i).padStart(3, '0')}.json`
  const rf = `${RDIR}/chunk_${String(i).padStart(3, '0')}.json`
  return agent(
    `${GUIDE}\n\nRead the chunk file ${cf} (a JSON array of functions, each with addr/size/apis/strs/c/existing_name). Document EVERY function in it. Then Write your results as a JSON array to ${rf} — each element {addr, name, purpose, confidence} — AND return the same array via the structured schema. Copy addr strings verbatim from the input. Do not skip any function.`,
    { label: `chunk_${i}`, phase: 'Document', effort: 'high', schema: SCHEMA }
  ).then(r => ({ i, n: r?.entries?.length || 0 }))
}))

const ok = results.filter(Boolean)
log(`documented ${ok.reduce((s, r) => s + r.n, 0)} functions across ${ok.length}/${CHUNKS} chunks`)
return ok
