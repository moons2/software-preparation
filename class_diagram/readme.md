# Class Diagram

**Classes** : an abstraction of an entitie in the real world

**Association** : relationship between classes

## Active Classes

Active classes initiate and represents actions or a flow of activity.

Active Classes are represented with thiker border.

## Passive Classes

Passive classes store and define data types, also serve other classes.

## Visibility

Methods and attributes visibilities are represented by signs

| Marker | Visibility |                        Explanation                         |
<<<<<<< HEAD
| :----: | :--------: | :--------------------------------------------------------: |
|   +    |   Public   |       available for classes ouside of the same class       |
|   -    |  Private   | hided from any class/object which is not of the same class |
|   #    | Protected  |            Only accessible by children classes             |
|   #    |  Package   |                                                            |
=======
| ------ | :--------: | :--------------------------------------------------------: |
| +      |   Public   |       available for classes ouside of the same class       |
| -      |  Private   | hided from any class/object which is not of the same class |
| #      | Protected  |            Only accessible by children classes             |
| #      |  Package   |                                                            |
>>>>>>> fce927b8a437975244a9e2a523fbc7aaea04f8a7

## Associations

Represent the way each class sees each other, put the name of the association above, on
or below the association line.

Place roles near each class to indicate what the association means.

## Multiplicity

Just a way to denote the amount of classes that makes relations with each other.

| indicator |  Meaning  |
| :-------: | :-------: |
|   0..1    |  0 or 1   |
|     1     | only one  |
|   0..\*   | 0 or more |

## Constraint

Place constraints inside curly braces ({})

## Compostion and Aggregation
