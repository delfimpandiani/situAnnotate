# Results Table

Note: Scroll horizontally to see expected results, actual results, and test result.
<table>
  <tr>
    <th>Competency Question</th>
    <th>SPARQL Query</th>
    <th>Expected Result</th>
    <th>Actual Result</th>
    <th>Passed</th>
  </tr>
  <tr>
    <td>CQ1: Which countries have been the location of annotation situations, how many annotation situations were located in each country, and which country has been the location for the highest number of annotation situations?</td>
    <td>
      <pre>
SELECT ?Country (COUNT(?AnnotationSituation) AS ?count)
WHERE {
    ?AnnotationSituation :atPlace ?Country .
}
GROUP BY ?Country
ORDER BY DESC(?count)
      </pre>
    </td>
    <td>
      <pre>
{
  "head": {
    "vars": [
      "Country",
      "count"
    ]
  },
  "results": {
    "bindings": [
      {
        "Country": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Italy"
        },
        "count": {
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "type": "literal",
          "value": "8"
        }
      }
    ]
  }
}
      </pre>
    </td>
    <td>
      <pre>
{
  "head": {
    "vars": [
      "Country",
      "count"
    ]
  },
  "results": {
    "bindings": [
      {
        "Country": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Italy"
        },
        "count": {
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "type": "literal",
          "value": "8"
        }
      }
    ]
  }
}
      </pre>
    </td>
    <td>YES</td>
  </tr>
<tr>
  <td>CQ2: Between the years 2020 and 2024, in which annotation situations has the image with ID "ARTstract_14978" been involved?</td>
  <td>
    <pre>
SELECT ?AnnotationSituation
WHERE {
    :ARTstract_14978 :isInvolvedInAnnotationSituation ?AnnotationSituation .
    ?AnnotationSituation :onDate ?Date .
    FILTER(YEAR(?Date) >= 2020 && YEAR(?Date) <= 2024)
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "AnnotationSituation"
    ]
  },
  "results": {
    "bindings": [
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_act_2023_06_28"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_age_2023_06_26"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_as_2023_06_26"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_color_2023_06_26"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_em_2023_06_26"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_ic_2023_06_28"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_od_2023_06_28"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "AnnotationSituation"
    ]
  },
  "results": {
    "bindings": [
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_act_2023_06_28"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_age_2023_06_26"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_as_2023_06_26"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_color_2023_06_26"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_em_2023_06_26"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_ic_2023_06_28"
        }
      },
      {
        "AnnotationSituation": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_od_2023_06_28"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>YES</td>
</tr>

<tr>
  <td>CQ3: What remuneration schemes have been used in annotation situations involving the "ARTstract" dataset?</td>
  <td>
    <pre>
SELECT ?RemunerationScheme 
WHERE {
    ?AnnotationSituation rdf:type :AnnotationSituation ;
    :involvesDataset :ARTstract .
    ?AnnotationSituation :involvesRemunerationScheme ?RemunerationScheme .
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "RemunerationScheme"
    ]
  },
  "results": {
    "bindings": []
  }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "RemunerationScheme"
    ]
  },
  "results": {
    "bindings": []
  }
}
    </pre>
  </td>
  <td>YES</td>
</tr>

<tr>
  <td>CQ4: What types of entities have been annotated?</td>
  <td>
    <pre>
SELECT DISTINCT ?EntityType 
WHERE {
    ?Annotation :aboutAnnotatedEntity ?Entity .
    ?Entity a ?EntityType .
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "EntityType"
    ]
  },
  "results": {
    "bindings": [
      {
        "EntityType": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Entity"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Image"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "http://www.ontologydesignpatterns.org/ont/dul/dul.owl#Entity"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "http://www.ontologydesignpatterns.org/ont/dul/dul.owl#InformationEntity"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#InformationEntity"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "http://www.ontologydesignpatterns.org/ont/dul/dul.owl#InformationObject"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#InformationObject"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "EntityType"
    ]
  },
  "results": {
    "bindings": [
      {
        "EntityType": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Entity"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Image"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "http://www.ontologydesignpatterns.org/ont/dul/dul.owl#Entity"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "http://www.ontologydesignpatterns.org/ont/dul/dul.owl#InformationEntity"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#InformationEntity"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "http://www.ontologydesignpatterns.org/ont/dul/dul.owl#InformationObject"
        }
      },
      {
        "EntityType": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#InformationObject"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>YES</td>
</tr>

<tr>
  <td>CQ5: Which images have been annotated using the lexical entry "surfboard," and what role did these annotations serve?</td>
  <td>
    <pre>
SELECT ?Image ?AnnotationRole
WHERE {
  ?Annotation :aboutAnnotatedEntity ?Image .
  ?Annotation :annotationWithLexicalEntry :le_surfboard .
  ?Annotation :isClassifiedBy ?AnnotationRole .
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Image",
      "AnnotationRole"
    ]
  },
  "results": {
    "bindings": [
      {
        "Image": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_14978"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Image",
      "AnnotationRole"
    ]
  },
  "results": {
    "bindings": [
      {
        "Image": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_14978"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>YES</td>
</tr>

<tr>
  <td>CQ6: For the specific situation in which "surfboard" was used to annotate the image with ID "ARTstract_14978," what contextual factors were associated with the annotation situation, including the country, date, annotated dataset, remuneration scheme, detection threshold, and comprehensive annotator details?</td>
  <td>
    <pre>
SELECT ?Country ?Date ?Dataset ?RemunerationScheme ?DetectionThreshold ?Annotator ?PretrainDataset ?ModelArchitecture
WHERE {
    ?Annotation :aboutAnnotatedEntity :ARTstract_14978 .
    ?Annotation :annotationWithLexicalEntry :le_surfboard .
    ?AnnotationSituation :involvesAnnotation ?Annotation .

    OPTIONAL {
        ?AnnotationSituation :atPlace ?Country .
        ?AnnotationSituation :onDate ?Date .
        ?AnnotationSituation :involvesDataset ?Dataset .
        ?AnnotationSituation :hasDetectionThreshold ?DetectionThreshold .
        ?AnnotationSituation :involvesAnnotator ?Annotator .
        ?Annotator :pretrainedOnDataset ?PretrainDataset .
        ?Annotator :hasModelArchitecture ?ModelArchitecture .
        ?AnnotationSituation :involvesRemunerationScheme ?RemunerationScheme .
    }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Country",
      "Date",
      "Dataset",
      "RemunerationScheme",
      "DetectionThreshold",
      "Annotator",
      "PretrainDataset",
      "ModelArchitecture"
    ]
  },
  "results": {
    "bindings": [
      {
        "Country": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Italy"
        },
        "Date": {
          "datatype": "http://www.w3.org/2001/XMLSchema#date",
          "type": "literal",
          "value": "2023-06-28"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract"
        },
        "DetectionThreshold": {
          "type": "literal",
          "value": "0.7"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#facebook_detr-resnet-101"
        },
        "PretrainDataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#COCO-dataset"
        },
        "ModelArchitecture": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detection_transformer"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Country",
      "Date",
      "Dataset",
      "RemunerationScheme",
      "DetectionThreshold",
      "Annotator",
      "PretrainDataset",
      "ModelArchitecture"
    ]
  },
  "results": {
    "bindings": [
      {
        "Country": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Italy"
        },
        "Date": {
          "datatype": "http://www.w3.org/2001/XMLSchema#date",
          "type": "literal",
          "value": "2023-06-28"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract"
        },
        "DetectionThreshold": {
          "type": "literal",
          "value": "0.7"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#facebook_detr-resnet-101"
        },
        "PretrainDataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#COCO-dataset"
        },
        "ModelArchitecture": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detection_transformer"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>YES</td>
</tr>

<tr>
  <td>CQ7: Which images have annotations classified under the role of "detected emotion" with an annotation strength exceeding 0.85, and what labels have been assigned to them?</td>
  <td>
    <pre>
SELECT ?Image ?Label
WHERE {
    ?Image a :Image .
    ?Annotation :aboutAnnotatedEntity ?Image ;
                :isClassifiedBy :detected_emotion ;
                :hasAnnotationStrength ?AnnotationStrength ;
                :annotationWithLexicalEntry ?LE .
    ?LE rdfs:label ?Label .
    FILTER (?AnnotationStrength > 0.55)
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Image",
      "Label"
    ]
  },
  "results": {
    "bindings": [
      {
        "Image": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_14978"
        },
        "Label": {
          "type": "literal",
          "value": "contentment"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Image",
      "Label"
    ]
  },
  "results": {
    "bindings": [
      {
        "Image": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract_14978"
        },
        "Label": {
          "type": "literal",
          "value": "contentment"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>YES</td>
</tr>

<tr>
  <td>CQ8: For the image with ID "ARTstract_14978," what concepts type annotations? Additionally, for each concept, what is the annotation strength and the annotation role of the annotation that was associated with it?</td>
  <td>
    <pre>
SELECT ?Concept ?AnnotationRole ?AnnotationStrength
WHERE {
    ?Annotation :aboutAnnotatedEntity :ARTstract_14978 .
    ?Annotation :isClassifiedBy ?AnnotationRole .
    ?Annotation :hasAnnotationStrength ?AnnotationStrength .
    ?Annotation :typedByConcept ?Concept .
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Concept",
      "AnnotationRole",
      "AnnotationStrength"
    ]
  },
  "results": {
    "bindings": [
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/running"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_action"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.9970308542251587"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/twenties"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_age"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.3349549472332001"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/impressionism"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_art_style"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.6149182915687561"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/contentment"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_emotion"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.5551347732543945"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/human"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_human_presence"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.7582577436257694"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.999"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/surfboard"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.962"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.988"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.996"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.999"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.92"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "1.0"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Concept",
      "AnnotationRole",
      "AnnotationStrength"
    ]
  },
  "results": {
    "bindings": [
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/running"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_action"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.9970308542251587"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/twenties"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_age"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.3349549472332001"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/impressionism"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_art_style"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.6149182915687561"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/contentment"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_emotion"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.5551347732543945"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/human"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_human_presence"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.7582577436257694"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.999"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/surfboard"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.962"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.988"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.996"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.999"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.92"
        }
      },
      {
        "Concept": {
          "type": "uri",
          "value": "http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/person"
        },
        "AnnotationRole": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#detected_object"
        },
        "AnnotationStrength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "1.0"
        }
      }
    ]
  }
}
    </pre>
  </td>
    <td>YES</td>
</tr>

<tr>
  <td>CQ9: For each lexical entry (label) that the image with ID "ARTstract_14978" was annotated with, who was the Annotator that assigned that label?</td>
  <td>
    <pre>
SELECT ?string ?Annotator 
WHERE {
    :ARTstract_14978 :isInvolvedInAnnotationSituation ?AnnotationSituation .
    ?AnnotationSituation :involvesAnnotation ?Annotation .
    ?AnnotationSituation :involvesAnnotator ?Annotator .
    ?Annotation :aboutAnnotatedEntity :ARTstract_14978.
    ?Annotation :annotationWithLexicalEntry ?LexicalEntry .
    ?LexicalEntry rdfs:label ?string .
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "string",
      "Annotator"
    ]
  },
  "results": {
    "bindings": [
      {
        "string": {
          "type": "literal",
          "value": "running"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#DunnBC22_vit-base-patch16-224-in21k_Human_Activity_Recognition"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "20-29"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#nateraw_vit-age-classifier"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "Impressionism"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#oschamp_vit-artworkclassifier"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "silver"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ColorThief"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "dimgray"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ColorThief"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "gray"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ColorThief"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "contentment"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#artemis_image-emotion-classifier"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "True"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#adhamelarabawy_fashion_human_classifier"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "person"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#facebook_detr-resnet-101"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "surfboard"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#facebook_detr-resnet-101"
        }
      }
    ]
  }
}
    </pre>
  </td>
 <td>
    <pre>
{
  "head": {
    "vars": [
      "string",
      "Annotator"
    ]
  },
  "results": {
    "bindings": [
      {
        "string": {
          "type": "literal",
          "value": "running"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#DunnBC22_vit-base-patch16-224-in21k_Human_Activity_Recognition"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "20-29"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#nateraw_vit-age-classifier"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "Impressionism"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#oschamp_vit-artworkclassifier"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "silver"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ColorThief"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "dimgray"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ColorThief"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "gray"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ColorThief"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "contentment"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#artemis_image-emotion-classifier"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "True"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#adhamelarabawy_fashion_human_classifier"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "person"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#facebook_detr-resnet-101"
        }
      },
      {
        "string": {
          "type": "literal",
          "value": "surfboard"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#facebook_detr-resnet-101"
        }
      }
    ]
  }
}
    </pre>
  </td>
<td> YES </td></tr>
<tr>
  <td>CQ10: What types of annotations about the image with ID "ARTstract_14978" were all done by artificial annotators with the "visual transformer" model architecture? Additionally, for each of these annotators, what dataset were they pretrained on, if applicable?</td>
  <td>
    <pre>
SELECT ?AnnotationClass ?Annotator ?Dataset
WHERE {
    ?AnnotationSituation :involvesAnnotation ?Annotation .
    ?AnnotationSituation :involvesAnnotator ?Annotator .
    ?Annotator :hasModelArchitecture :visual_transformer .
    ?Annotator :pretrainedOnDataset ?Dataset .
    ?Annotation :aboutAnnotatedEntity :ARTstract_14978 .
    ?Annotation a ?AnnotationClass .

    FILTER NOT EXISTS {
        ?subClass rdfs:subClassOf ?AnnotationClass .
        ?Annotation rdf:type ?subClass.
        FILTER (?subClass != ?AnnotationClass)
    }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "AnnotationClass",
      "Annotator",
      "Dataset"
    ]
  },
  "results": {
    "bindings": [
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ActionAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#DunnBC22_vit-base-patch16-224-in21k_Human_Activity_Recognition"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#har-dataset"
        }
      },
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#AgeAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#nateraw_vit-age-classifier"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#fair-face"
        }
      },
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ArtStyleAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#oschamp_vit-artworkclassifier"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#artbench-10"
        }
      },
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#HumanPresenceAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#adhamelarabawy_fashion_human_classifier"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#deep-fashion-v1"
        }
      },
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ImageCaptionAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Salesforce_blip-image-captioning-large"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#COCO-dataset"
        }
      }
    ]
  }
}
    </pre>
  </td>
    <td>
    <pre>
{
  "head": {
    "vars": [
      "AnnotationClass",
      "Annotator",
      "Dataset"
    ]
  },
  "results": {
    "bindings": [
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ActionAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#DunnBC22_vit-base-patch16-224-in21k_Human_Activity_Recognition"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#har-dataset"
        }
      },
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#AgeAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#nateraw_vit-age-classifier"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#fair-face"
        }
      },
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ArtStyleAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#oschamp_vit-artworkclassifier"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#artbench-10"
        }
      },
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#HumanPresenceAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#adhamelarabawy_fashion_human_classifier"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#deep-fashion-v1"
        }
      },
      {
        "AnnotationClass": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ImageCaptionAnnotation"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Salesforce_blip-image-captioning-large"
        },
        "Dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#COCO-dataset"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td> YES </td>
</tr>

<tr>
  <td>CQ11: What are the caption annotations for the image with ID "ARTstract_14978," and who are the annotators responsible for each caption annotation?</td>
  <td>
    <pre>
SELECT ?Caption ?Annotator
WHERE {
    ?Annotation :aboutAnnotatedEntity :ARTstract_14978 .  
    ?Annotation a :ImageCaptionAnnotation .
    ?Annotation rdfs:comment ?Caption .
    ?AnnotationSituation :involvesAnnotation ?Annotation .
    ?AnnotationSituation :involvesAnnotator ?Annotator .
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Caption",
      "Annotator"
    ]
  },
  "results": {
    "bindings": [
      {
        "Caption": {
          "type": "literal",
          "value": "painting of children playing in the water at the beach"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Salesforce_blip-image-captioning-large"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>
    <pre>
{
  "head": {
    "vars": [
      "Caption",
      "Annotator"
    ]
  },
  "results": {
    "bindings": [
      {
        "Caption": {
          "type": "literal",
          "value": "painting of children playing in the water at the beach"
        },
        "Annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Salesforce_blip-image-captioning-large"
        }
      }
    ]
  }
}
    </pre>
  </td>
  <td>YES</td>
</tr>



</table>
