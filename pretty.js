

let x = { './testdir/childdir': { 'files': [{ 'fingerprint': 'd41d8cd98f00b204e9800998ecf8427e', 'parent': 'e', 'filename': 'test.js' }], 'daughters_nicknames': [], 'nickname': 'e', 'parent': './testdir', 'daughters': [] }, './directory_with_no_children_dirs': { 'files': [{ 'fingerprint': 'd41d8cd98f00b204e9800998ecf8427e', 'parent': 'c', 'filename': 'dummyfile.js' }], 'daughters_nicknames': [], 'nickname': 'c', 'parent': '.', 'daughters': [] }, './testdir': { 'files': [{ 'fingerprint': 'd41d8cd98f00b204e9800998ecf8427e', 'parent': 'd', 'filename': 'aaa.js' }], 'daughters_nicknames': ['e'], 'nickname': 'd', 'parent': '.', 'daughters': ['./testdir/childdir'] }, '.': { 'files': [{ 'fingerprint': '0e48715808c39b10ecc200d97a8ef4c1', 'parent': 'b', 'filename': 'RecursiveFileFingerprinter.py' }, { 'fingerprint': '6a9ac83f3bdf334c6d40c3b7557d1a4c', 'parent': 'b', 'filename': 'pretty.js' }, { 'fingerprint': '5ca6b0e4a5a89783032158f9a4c41492', 'parent': 'b', 'filename': 'get_id.py' }], 'daughters_nicknames': ['c', 'd'], 'nickname': 'b', 'parent': '', 'daughters': ['./directory_with_no_children_dirs', './testdir'] } }



console.log(JSON.stringify(x, null, 2))
