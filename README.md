# button-slam-filler
Database population scripts for Button Slam, an upcoming alexa skill. 

#setup
1. Install conda / python 3.6.
2. Clone button-slam-filler into your workspace.
3. Create a new conda environment based on the environmnt file that I export.  

   Use the command ```conda env create -f environment.yml``` to install the python dependencies that I use. 

   To export the existing environment, use ```conda env export > environment.yml```

4. (Actually works) I couldn't figure out how to get it all to work with conda, so I did the following commands

   ```conda install pip```

   ```pip install virtualenv```

   ```pip install beautifulsoup4 -t ~/path/to/directory```
   

