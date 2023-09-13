# maxwells-information-demon
The goal of this repo is to convert problems to their highest possible density. I believe a tool that could do this would help computational systems logically solve problems that are given in natural language.

Example 1:
```
input_sentence = 'A block of mass 5.0 kg is pushed across a horizontal surface by a horizontal force of 20 N. If the frictional force between the block and the surface is 8.0 N, what is the acceleration of the block?'
---
answer = 'desired_variable=acceleration;mass=5.0;horizontal_force=20;frictional_force=8.0;acceleration=??;net_force_formula=horizontal_force-frictional_force;acceleration_formula=net_force/mass'
```
Example 2:
```
input_sentence = 'Albert has 10 apples. Laura has 4 apples. Albert gives Laura 5 apples. how many more apples does albert have than laura?'
---
answer = 'desired_variable=albert_apples_more_than_laura;albert_initial_apples=10;laura_initial_apples=4;apples_given=5;albert_final_apples=albert_initial_apples-apples_given;laura_final_apples=laura_initial_apples+apples_given;albert_apples_more_than_laura=albert_final_apples-laura_final_apples'
```

## How to use
1. Edit the path variable in src/config.py

2. Edit the question asked in src/condense.py