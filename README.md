# pyVideoHash
Perceptual hashing for videos / images

### What does the code do in this state?
It reads in an hardcoded (path set in video_hash.py) media file, calculates a perceptual video-hash (which is quite robust to noise and geometric transformations) and outputs this perceptual-hash with an additional file-hash into an sqlite-database.

The perceptual-hash consists of 144bits for each frame. 

### What is needed to run above functionality?
#### Requirements / External libraries to install (tested with Python 2.7.11)
- numpy: various array-stuff
- moviepy: video-reading
- skimage: image-tranformations
- scikit-learn: min-max-scaling
- deltasigma: quantization
- bitstring: bit-arrays
- peewee: database-handling
- cython: acceleration of cumulant-code (cython will compile whole frame_hash.pyx)

#### Database-setup
See peewee-docs.

#### Cython-compilation
This is done automatically when setup.py is run with argument "install"

### Speed:
The code is not very much optimized and is running on one core only. I obtain ~3fps on 720p-h264 (~ 1/10 realtime-processing) which is quite slow.
