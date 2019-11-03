# Faces: the Backlog

Hint: use this backlog in your commits: when taking up a story, change 'TODO' to 'DOING', when ready, change it to 'DONE'.

1. DONE: I want to run a program that draws me a face.  This face can be the same one every single time.
    * It can be a command line program e.g. `face.py`.
    * The face should have an outline.
    * The face should have two eyes and a mouth.
2. DONE: I want to specify if the face should have a nose or not, so that I can use it as a simplified emoji.
    * This should be specified as a command line parameter `--nose=[none|.|o|O|v]`.
3. DONE: I want to specify the size of my paper in rows and columns, and the face should grow with it.
    * The face should be on the center of the page
    * The page outline can be made visual with `--paper_outline`, but is invisible otherwise
4. TODO: I want to specify the feeling of the face.
    * With a parameter `--feeling=[happy|sad]`
5. TODO: I want to specify the shape of the face.
    * With a parameter `--face_shape=[round|square]`
    * (note: the egg and trapezium are great candidates for hotfix releases later on: upside down/horizontal/vertical)
6. TODO: I want to specify the type of eyes.
    * With a parameter `--eyes={ab}` where a is the character to use for the left eye, b for the right eye: xX, oo, -o, O-, ...
7. TODO: I want to specify the hair.
    * With a parameter `--hair=[bald|pointy]`
8. TODO: I want to specify the shape of the face to be egg-like.
    * With a parameter `--face_shape=egg`
9. TODO: I want to specify the jaws and chin.
    * With a parameter `--jaws=[wide|narrow|pointy]`
