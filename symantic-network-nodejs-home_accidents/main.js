var expert = require('expert');
var _ = require('underscore');

var domain   = expert.Domain(),
    Concept  = domain.Concept,
    Relation = domain.Relation;

var accident = Concept.create({id:"accident"}),
    chute = Concept.create({id:"chute"}),
    brulure = Concept.create({id:"brulure"});
    nosee = Concept.create({id:"nosee"});
    fracture = Concept.create({id:"fracture"});
    douleur = Concept.create({id:"douleur"});


var isa = domain.isa,
    example = domain.example;

var has = Relation.create({id:"has"}),
    whatHas = Relation.create({id:"what has",inverseFor:has});

// Examples
fracture
  .isa(accident)
  .has(nosee)
  .has(douleur)

brulure
  .isa(accident)
  .has(douleur)

console.log("What has fracture?");
console.log(whatHas(douleur));
