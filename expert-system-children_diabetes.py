#!/usr/bin/env python
# # -*- coding: utf-8 -*-

from pyknow import *

"""
    Expert system for detecting if an enfant is diabetic
    @author: Fortas Abdeldjalil.
    Thanks to Chawki Benchehida for the introduction to PyKe.
    Helpful Ressources:
        * http://www.nospetitsmangeurs.org/quoi-faire-si-mon-enfant-a-le-diabete/
        * http://www.nospetitsmangeurs.org/les-hauts-et-les-bas-du-taux-de-sucre/
        * http://www.childrenshospital.org/conditions-and-treatments/conditions/hypoglycemia-and-low-blood-sugar/symptoms-and-causes

"""

class Personne(Fact):
    """Info about the patient"""
    pass

class InreferenceEngine(KnowledgeEngine):
    @Rule()
    def personne_concernee(self):
            if self.facts[1]['age'] <= 5:
                self.declare(Fact(concerned=True))

    @Rule(Fact(concerned=True))
    def hyper_glycemy(self):
        if (self.facts[1]['glycemie'] > 10):
            self.declare(Fact(hyperglycemic_risk=True))
            print("Warning! High blood sugar")
        else:
            self.declare(Fact(hyperglycemic_risk=False))

    @Rule(Fact(concerned=True))
    def hypo_glycemy(self):
        if (self.facts[1]['glycemie'] < 4):
            print("Warning! Low blood sugar")
            self.declare(Fact(hypoglycemic_risk=True))
        else:
            self.declare(Fact(hypoglycemic_risk=False))

    @Rule(Fact(concerned=True))
    def has_signs_low_sugar(self):
        if sum([
                self.facts[1]['shakiness'],
                self.facts[1]['hunger'],
                self.facts[1]['sweating'],
                self.facts[1]['headach'],
                self.facts[1]['pale'],
                ]) > 3:
            self.declare(Fact(has_signs_low_sugar=True))


    # If the patient is a child and has one or many signes or his blood sugar level is low
    @Rule(Fact(concerned=True), Fact(has_signs_low_sugar=True))
    def protocole_risk(self):
        print("The child has some signs of low blood sugar")

    # If the patient is a child and has one or many signes, and his blood sugar level is low
    @Rule(Fact(concerned=True), Fact(hypoglycemic_risk=True), Fact(has_signs_low_sugar=True))
    def protocole_alert(self):
        print("Alert! High risk of diabetes, you must see a doctor")

    ## TODO Add high blood sugar signs

engine = InreferenceEngine()
engine.reset()

# Initial facts
engine.declare(Personne(age=2,
                        glycemie=3,
                        shakiness= True,
                        hunger= True,
                        sweating= True,
                        headach= True,
                        pale= True,
                        ))
engine.run()
