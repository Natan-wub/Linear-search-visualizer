---
Algorithm: Linear Search, I chose this search algorithm as it seemed the simplest to impliment and teach by means of visualization.
## Demo video/gif/screenshot of test
Testing and Verification

1.First testing of draft Algorithm the does not account for edge cases.

![Linear Search - Static test](https://github.com/user-attachments/assets/3c6cec7f-b995-40d9-a421-97a05a257f25)



2. Attempting to fix edge cases (non integer user input ) and adding animation, ended up with an error message as I discovered the method I used to add animation (HTML embedded animation) is not supported by Hugging face. We can also see that the algorithm does not clearly show if  the target is absent in words.
User input error:

![Linear Search - static, invalid input](https://github.com/user-attachments/assets/58f03a8f-1a1c-4e1c-a504-a513771151fd)

Animation failure:

![Linear Search Animation failure ](https://github.com/user-attachments/assets/c65a7a31-f67e-4089-a5c0-2e44e37cb586)



3. Managed to account for the user input error by adding a feature where if the input was anything else other than a string of integers it returns an “invalid input” message instead. For the animation I ended up implementing the animation and a GIF instead as that's what hugging face is able to support. To do this I had to install an additional dependency called “pillow” for the animation. I also ended up using this same creature to account for when the target is not found instead of showing the lack of verification “green bar” it instead turns all the bars to red indicating the target wasn't found and reuters a “target not found” message
Final testing:

![Linear Search - a Hugging Face Space by NatanWub - Google Chrome 2025-12-05 22-20-44](https://github.com/user-attachments/assets/7bf68b83-bc60-472e-af21-569133eb010b)

## Problem Breakdown & Computational Thinking (You can add a flowchart and write the

Decomposition: The linear search algorithm is composed the following steps 
1. Take the array input.
2. Iterate through elements one by one.
3. Compare each element to the target.
4. Return the index if found, or indicate “not found.”
 
• Pattern Recognition: The search pattern is repetitive meaning it repeats the same step of moving one index then comparing 
• Abstraction: For this algorithm we should just focus on the comparison between the array and the target and not the actual value of the array, it will work with what ever type of input we decide to implement.
• Algorithm Design: 
1. After taking in input from the user start at index 0.
2. Compare element with target.
3. If equal –  return index.
4. If not equal -- move to next index.
5. Repeat until the end of the array.
6. If no match –  return “not found.

Flow chart:
<img width="1431" height="444" alt="Screenshot 2025-12-05 210830" src="https://github.com/user-attachments/assets/0c815e98-7ac4-4e7c-ae32-613fb6dadaaa" />

## Steps to Run
The steps the code takes through out the searhing is as follows:
- Validate input - parse numbers.
- Draw bars - animate checking each element.
- Show match in green or all-red if not found.
- Hold the final frame longer, run once, and return a GIF + status message via the GUI.

## Hugging Face Link:
 https://huggingface.co/spaces/NatanWub/Linear_search

## Author & Acknowledgment:
This project is a collaboration between me (Natan Atnafu) and AI (Copilot AI), throughout the project aside for the basic linear search algorithm, which i wrote from what i learned on implementation of linear search, i used level 4 AI to help me debug and implement the Gradio and pillow GUI, throughout each error and confusion on what the purpose of a certain line pf code was i would as copilot to elaborate and offer solutions, from with i would take test and implement in to my code. 










