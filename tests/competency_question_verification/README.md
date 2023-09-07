# Competency Questions as Evaluation Tools

## Competency Questions

## Competency Questions

Competency questions (CQs) serve as a fundamental component in the evaluation of ontologies [^1], and we use them to evaluate our ontology, SituAnnotate. These carefully crafted questions guide our assessment of the ontology's capability to model, represent, and retrieve essential information about situated data labels. In this section, we provide an overview of eleven competency questions, covering details about annotation situations, annotations, and annotators.

### Geographic Distribution of Annotation Situations

**CQ1:** *Which countries have been the location of annotation situations, how many annotation situations were located in each country, and which country has been the location for the highest number of annotation situations?*

*Rationale:* This competency question sheds light on the geographic scope of annotation situations captured by SituAnnotate. Understanding where annotation activities are concentrated can provide insights into regional preferences, data availability, and potential biases in the annotation process.

### Temporal Filtering of Annotation Situations

**CQ2:** *In a specific period of time, in which annotation situations has a specific image been involved?*

*Rationale:* This question tests SituAnnotate's ability to track temporal information to enable precise filtering based on annotation dates. This feature also facilitates the comparison of annotations before and after significant cultural moments, such as the COVID-19 pandemic, offering insights into how labels for the same image may evolve over time in response to societal changes.

### Remuneration Schemes in Annotation Situations

**CQ3:** *What remuneration schemes have been used in annotation situations involving a certain dataset?*

*Rationale:* This question explores the various compensation models employed in annotation situations that have led to annotations for a specific dataset. Identifying remuneration schemes informs us about the motivations and incentives driving annotators, which can impact the quality and consistency of annotations.

### Annotated Entity Types in Annotation Situations

**CQ4:** *What types of entities have been annotated?*

*Rationale:* This query illuminates the entities whose annotations have been integrated into the SituAnnotate ontology. It offers insight into the categories of entities, such as images and documents, that have undergone annotation and are represented within the SituAnnotate knowledge graph. This comprehension is crucial for domain-specific applications as it unveils the breadth of concepts encompassed by the ontology.

### Identifying Annotations based on Lexical Entry

**CQ5:** *Which entities have been annotated using a specific lexical entry, and what role did these annotations serve?*

*Rationale:* This question exemplifies how the ontology can be leveraged for the identification of all entities, or entities of a specific type (e.g., images), that have been annotated with the same lexical entry (e.g., "surfboard") and the corresponding annotation roles (e.g., detected object). This query is instrumental in gaining insights into the usage and impact of specific lexical entries across various annotations.

### Identifying Contextual Information for Annotations

**CQ6:** *For a specific situation in which a lexical entry was used to annotate an entity, what contextual factors were associated with the annotation situation, including the country, date, annotated dataset, remuneration scheme, detection threshold, and comprehensive annotator details?*

*Rationale:* This question aims to provide comprehensive context for a particular annotation scenario, encompassing geographical and temporal aspects, the dataset under annotation, remuneration specifics, detection thresholds, and annotator attributes. It offers a powerful tool for understanding how a ground truth is situated within its originating context.

### Filtering Annotations by Reliability and Roles

**CQ7:** *Which entities have annotations classified under a specific annotation role with an annotation strength exceeding a certain threshold, and what labels have been assigned to them?*

*Rationale:* This question delves into annotations categorized by specific roles (e.g., detect object, detected emotion, detected action) and their associated annotation strengths. It allows for the filtering of entities based on the reliability or strength of annotations and provides insight into the specific labels assigned to these entities.

### Identifying Concepts Typing Annotations about Entities

**CQ8:** *What concepts type annotations about a specific entity? Additionally, for each concept, what is the annotation strength and the annotation role of the annotation that was associated with it?*

*Rationale:* This question focuses on the concepts linked to annotations for a particular entity, delving into the specifics of typed annotations. It not only provides a list of concepts associated with an entity via situated annotations but also essential details about the nature of these assignments, such as their roles (e.g., detected emotion or detected action, etc.) and the strength of these associations. This nuanced view enhances our understanding of the annotations' semantics and reliability.

### Tracking Annotators Responsible for Annotation Labels

**CQ9:** *For each lexical entry (label) that a certain entity image was annotated with, who was the Annotator that assigned that label?*

*Rationale:* This question delves into the identification of the annotators accountable for specific labels associated with a particular image. This level of detail enables the attribution of annotations to individual annotators, facilitating an assessment of their contributions.

### Artificial Annotators and Shared Model Architectures

**CQ10:** *What types of annotations about an entity were all done by artificial annotators with a specific model architecture? Additionally, for each of these annotators, what dataset were they pretrained on, if applicable?*

*Rationale:* This question explores artificial annotators that employ a shared architectural backbone for creating annotations of various types. Identifying shared model architectures sheds light on the integration of automated annotation tools within annotation pipelines. Additionally, it provides insights into the prevalence of specific model architectures and their pretraining on various datasets, contributing to a broader understanding of automated annotation methods.

### Identifying Image Caption Annotations and Annotators

**CQ11:** *What are the caption annotations for a specific image, and who are the annotators responsible for each caption annotation?*

*Rationale:* This query focuses on revealing caption annotations and their respective annotators for a given image. It is vital for examining the generation and attribution of textual descriptions, shedding light on the creators of these annotations and their role in conveying information about the image.

[^1]: Blomqvist, E., Sandkuhl, K., & Öhgren, A. (2010). Experimenting with ontology evaluation. In IFIP International Conference on Formal Ontologies in Information Systems (pp. 31-44).



## Specialized Competency Questions (CQs) with SPARQl queries

For each of the competency questions, we developed specialized versions of them and transformed each of them into SPARQL queries (See table \ref{tab:sparql}).

### Annotation Situations
- CQ1: Which countries have been the location of annotation situations, how many annotation situations were located in each country, and which country has been the location for the highest number of annotation situations?

```
SELECT ?Country (COUNT(?AnnotationSituation) AS ?count)
WHERE {
    ?AnnotationSituation :atPlace ?Country .
}
GROUP BY ?Country
ORDER BY DESC(?count)
```
- CQ2: Between the years 2020 and 2024, in which annotation situations has the image with ID "ARTstract_14978" been involved?

```
SELECT ?AnnotationSituation ?Date
WHERE {
    :ARTstract_14978 :isInvolvedInAnnotationSituation ?AnnotationSituation .
    ?AnnotationSituation :onDate ?Date .
    FILTER(YEAR(?date) >= 2020 && YEAR(?date) <= 2024)
}

```

- CQ3: What remuneration schemes have been used in annotation situations involving the "ARTstract" dataset?

```
SELECT ?RemunerationScheme 
WHERE {
    ?AnnotationSituation rdf:type :AnnotationSituation ;
    :involvesDataset :ARTstract .
    ?AnnotationSituation :involvesRemunerationScheme ?RemunerationScheme .
}
```

### Annotations

- CQ4: What types of entities have been annotated?

```
SELECT DISTINCT ?EntityType 
WHERE {
    ?Annotation :aboutAnnotatedEntity ?Entity .
    ?Entity a ?EntityType .
}

```

- CQ5: Which images have been annotated using the lexical entry "surfboard," and what role did these annotations serve?

```
SELECT DISTINCT ?EntityType 
WHERE {
    ?Annotation :aboutAnnotatedEntity ?Entity .
    ?Entity a ?EntityType .
}
```

- CQ6: For the specific situation in which "surfboard" was used to annotate the image with ID "ARTstract_14978," what contextual factors were associated with the annotation situation, including the country, date, annotated dataset, remuneration scheme, detection threshold, and comprehensive annotator details?

```
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

```

- CQ7: Which images have annotations classified under the role of "detected emotion" with an annotation strength exceeding 0.85, and what labels have been assigned to them?

```
SELECT ?Image ?Annotation ?Label ?AnnotationStrength
WHERE {
    ?Image a :Image .
    ?Annotation :aboutAnnotatedEntity ?Image ;
                :isClassifiedBy :detected_emotion ;
                :hasAnnotationStrength ?AnnotationStrength ;
                :annotationWithLexicalEntry ?LE .
    ?LE rdfs:label ?Label .
    FILTER (?AnnotationStrength > 0.85)
}

```

- CQ8: For the image with ID "ARTstract_14978," what concepts type annotations? Additionally, for each concept, what is the annotation strength and the annotation role of the annotation that was associated with it?

```
SELECT ?Concept ?AnnotationRole ?AnnotationStrength
WHERE {
    ?Annotation :aboutAnnotatedEntity :ARTstract_14978 .
    ?Annotation :isClassifiedBy ?AnnotationRole .
    ?Annotation :hasAnnotationStrength ?AnnotationStrength .
    ?Annotation :typedByConcept ?Concept .
}

```
### Annotators 

- CQ9: For each lexical entry (label) that the image with ID "ARTstract_14978" was annotated with, who was the Annotator that assigned that label?

```
SELECT ?string ?Annotator 
WHERE {
    :ARTstract_14978 :isInvolvedInAnnotationSituation ?AnnotationSituation .
    ?AnnotationSituation :involvesAnnotation ?Annotation .
    ?AnnotationSituation :involvesAnnotator ?Annotator .
    ?Annotation :aboutAnnotatedEntity :ARTstract_14978.
    ?Annotation :annotationWithLexicalEntry ?LexicalEntry .
    ?LexicalEntry rdfs:label ?string .
}

```

- CQ10: What types of annotations about the image with ID "ARTstract_14978" were all done by artificial annotators with the "visual transformer" model architecture? Additionally, for each of these annotators, what dataset were they pretrained on, if applicable?

```
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

```

- CQ11: What are the caption annotations for the image with ID "ARTstract_14978," and who are the annotators responsible for each caption annotation?

```
SELECT ?Caption ?Annotator
WHERE {
    ?Annotation :aboutAnnotatedEntity :ARTstract_14978 .  
    ?Annotation a :ImageCaptionAnnotation .
    ?Annotation rdfs:comment ?Caption .
    ?AnnotationSituation :involvesAnnotation ?Annotation .
    ?AnnotationSituation :involvesAnnotator ?Annotator .
}

```

