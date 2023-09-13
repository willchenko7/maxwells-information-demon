pre_prompt = '''
I am about to provide a question in natural language and I want you to isolate the variables and their values. 
If it is not known, just say variable=?? or provide the formula to calculate it. 
Please include any formulas inside the prompt in your answer. 
Please provide this is plain csv format with a start and stop token. 
Please also explicitly state which variable is being asked to solve for.
Be as explicit as possible, do not abbreviate any variable name.
Only provide the csv string, not need for anything else.
example: "<start>desired_variable=variable_three;variable_one=5;variable_two=7;variable_three=??<stop?". 
ok, here is the question: 
'''

question_0 = '"Albert has 10 apples. Laura has 4 apples. Albert gives Laura 5 apples. how many more apples does albert have than laura?"'
question_1 = '"A block of mass 5.0 kg is pushed across a horizontal surface by a horizontal force of 20 N. If the frictional force between the block and the surface is 8.0 N, what is the acceleration of the block?"'

prompt = pre_prompt + question_0
print('----')
print(prompt.replace('\n',''))
print('----')
