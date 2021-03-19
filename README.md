# What will this be?
3d project viewer

# TODO
Everything

# Stack
Python ( collect data ) and THREE.js to display results.

# exclude and include certain files:
See lines 26 and 63

# Gather the data from the python
python RecursiveFileFingerprinter.py  
  
Now you will have a big ball of json. Here is some cleaned up output ( thank to node's JSON.stringify() is pretty.js ):    
{  
  "./testdir": {  
    "nickname": 2,  
    "children": [  
      {  
        "fingerprint": "d41d8cd98f00b204e9800998ecf8427e",  
        "parent": 2,  
        "filename": "aaa.js"  
      }  
    ]  
  },  
  ".": {  
    "nickname": 1,  
    "children": [  
      {  
        "fingerprint": "6478a6c61efd904064bb83cd737aba9d",  
        "parent": 1,  
        "filename": "NextLetter.py"  
      },  
      {  
        "fingerprint": "e65917861737c331e68008efd9390c1d",  
        "parent": 1,  
        "filename": "RecursiveFileFingerprinter.py"  
      }  
    ]  
  }  
}  




