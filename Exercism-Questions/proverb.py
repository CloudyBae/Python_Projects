"""For want of a horseshoe nail, a kingdom was lost, or so the saying goes.
Given a list of inputs, generate the relevant proverb. 
For example, given the list ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"], you will output the full text of this proverbial rhyme:
For want of a nail the shoe was lost.
For want of a shoe the horse was lost.
For want of a horse the rider was lost.
For want of a rider the message was lost.
For want of a message the battle was lost.
For want of a battle the kingdom was lost.
And all for the want of a nail.
Note that the list of inputs may vary; your solution should be able to handle lists of arbitrary length and content. 
No line of the output text should be a static, unchanging string; all should vary according to the input given."""

def proverb(*args, qualifier=None):
    saying = [f"For want of a {args[i]} the {args[i+1]} was lost." for i in range(len(args)-1)]
     
    if len(args) > 0:                 
        if qualifier == None:
            saying.append(f"And all for the want of a {args[0]}.")  
        else:
            saying.append(f"And all for the want of a {qualifier} {args[0]}.")    

    return saying