# Knowledge representation examples

This repository contains some programming exercises for **Ontologies and Knowledge representation** class in University. It contains until the moment two examples:

* [Expert System that diagnosis children diabetes](expert-system-for-children-diabetes-diagnosis).
* Semantic network (home accidents as example) *unfinished yet*

## Expert System for children Diabetes Diagnosis

Built with Python, using [PyKnow]() library. And there's a tiny Node/Express server for offering a Web api
### Usage
* First install `pyknow` Python package, and `Express` and `python-shell` for Node.js, then lunch the server (`main.js`) in order to use the Web API.
All this could be done with this command:
`pip install pyknow && npm install && node main.js`
* Then open your browser, and past this URL for example.
```
localhost:3000/res/api?age=3
                        &glycemie=2
                        &shakiness=True
                        &hunger=True
                        &sweating=True
                        &headach=True
                        &diabetic_parents=False
                        &pale=False
                        &urination=False
                        &thirst=False
                        &blurred_vision=False
                        &dry_mouth=False
                        &smelling_breath=False
                        &shortness_of_breath=False
```
Now you can play with each parameter
  * age = [int from 0 to 5]
  * glycemie= [ int `mmol/l` ]
  * Signs, like shakiness, hunger, sweating..= [Boolean: True/False]

Or You can use the python file directly just introduce your facts manually

Change
```python
# ligne 102
engine.declare(Personne(age= int(sys.argv[1]),
                        glycemie=int(sys.argv[2]),
                        shakiness= bool(sys.argv[3]),
                        hunger= bool(sys.argv[4]),
                        sweating= bool(sys.argv[5]),
                        headach= bool(sys.argv[6]),
                        diabetic_parents = bool(sys.argv[7]),
                        pale= bool(sys.argv[8]),
                        urination = bool(sys.argv[9]),
                        thirst = bool(sys.argv[10]),
                        blurred_vision = bool(sys.argv[11]),
                        dry_mouth = bool(sys.argv[12]),
                        smelling_breath = bool(sys.argv[13]),
                        shortness_of_breath = bool(sys.argv[14]),
                        ))
```
To (for example)
```python
# ligne 102
engine.declare(Personne(age= 2,
                        glycemie=True,
                        shakiness=True,
                        hunger= True,
                        sweating= True,
                        headach= True,
                        diabetic_parents = False,
                        pale= False,
                        urination = False,
                        thirst = False,
                        blurred_vision = False,
                        dry_mouth = False,
                        smelling_breath = False,
                        shortness_of_breath = False,
                        ))
```
