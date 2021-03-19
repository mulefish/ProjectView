# What will this be?
3d project viewer. So for I've only written the python to collect information up into a JSON format. Later I will write the javascript view portion. 

# TODO
For the view? Everything. For collecting up the information? Maybe done. 

# Stack
Python ( collect data ) and THREE.js to display results.

# exclude and include certain files:
See lines 26 and 63

# Gather the data from the python
python RecursiveFileFingerprinter.py  
  
Now you will have a big ball of json. Here is some cleaned up output ( thanks to node's JSON.stringify() in pretty.js ):    
```yaml
{
  "./testdir/childdir": {
    "nickname": "e",
    "children": [
      {
        "fingerprint": "d41d8cd98f00b204e9800998ecf8427e",
        "parent": "e",
        "filename": "test.js"
      }
    ]
  },
  "./directory_with_no_children_dirs": {
    "nickname": "c",
    "children": [
      {
        "fingerprint": "d41d8cd98f00b204e9800998ecf8427e",
        "parent": "c",
        "filename": "dummyfile.js"
      }
    ]
  },
  "./testdir": {
    "nickname": "d",
    "children": [
      {
        "fingerprint": "d41d8cd98f00b204e9800998ecf8427e",
        "parent": "d",
        "filename": "aaa.js"
      }
    ]
  },
  ".": {
    "nickname": "b",
    "children": [
      {
        "fingerprint": "4139ce09f7488cf26f5835a0c181dad4",
        "parent": "b",
        "filename": "RecursiveFileFingerprinter.py"
      },
      {
        "fingerprint": "eef4ccfbc18cf915d5998c44dc83ce58",
        "parent": "b",
        "filename": "pretty.js"
      },
      {
        "fingerprint": "5ca6b0e4a5a89783032158f9a4c41492",
        "parent": "b",
        "filename": "get_id.py"
      }
    ]
  }
```



