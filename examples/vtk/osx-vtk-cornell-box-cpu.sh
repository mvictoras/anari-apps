
export ANARI_LIBRARY=ospray

# GPU test

export OSPRAY_LOAD_MODULES=cpu
export OSPRAY_DEVICE=cpu

export VTK_DEFAULT_EGL_DEVICE_INDEX=3

export DYLD_LIBRARY_PATH=~/src/ospray-apps/anari/install/lib:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=~/src/ospray-apps/anari-ospray/install/lib:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=~/src/ospray-apps/ospray/install/lib:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=~/src/ospray-apps/vtk/install/lib:$DYLD_LIBRARY_PATH
export PYTHONPATH=~/src/ospray-apps/vtk/install/lib/python3.12/site-packages:$PYTHONPATH
python vtk-cornell-box.py
