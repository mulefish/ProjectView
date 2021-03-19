

let x = { './testdir': { 'nickname': 2, 'children': [{ 'fingerprint': 'd41d8cd98f00b204e9800998ecf8427e', 'parent': 2, 'filename': 'aaa.js' }] }, '.': { 'nickname': 1, 'children': [{ 'fingerprint': '6478a6c61efd904064bb83cd737aba9d', 'parent': 1, 'filename': 'NextLetter.py' }, { 'fingerprint': 'e65917861737c331e68008efd9390c1d', 'parent': 1, 'filename': 'RecursiveFileFingerprinter.py' }] } }
console.log(JSON.stringify(x, null, 2))
