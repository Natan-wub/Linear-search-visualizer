import matplotlib.pyplot as plt
import matplotlib.animation as animation
import gradio as gr
import tempfile

def visualize_linear_search(array_str, target_str):
    try:
        # Try converting input into integers
        array = [int(x.strip()) for x in array_str.split(",")]
        target = int(target_str)
    except ValueError:
        return None, " >:( Invalid input: Please enter only integers separated by commas." #wrong input type leads to desplaying this message.
#bar colors
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(array)), array, color="lightblue")
    ax.set_title("Linear Search Visualization")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

    found_index = -1

    def update(frame):
        nonlocal found_index
        # Reset colors each frame
        for i, bar in enumerate(bars):
            if i == found_index:
                bar.set_color("green")
            else:
                bar.set_color("lightblue")

        # Highlight the current index
        bars[frame].set_color("orange")

        # If target found, mark green
        if array[frame] == target and found_index == -1:
            found_index = frame
            bars[frame].set_color("green")

        # If this is the last frame and target not found then turn all red (implimented last)
        if frame == len(array) - 1 and found_index == -1:
            for bar in bars:
                bar.set_color("red")
#animation part
    ani = animation.FuncAnimation(
        fig, 
        update,  
        frames=list(range(len(array))) + [len(array)-1]*5,  # repeat last frame 5 time
        interval=800,
        repeat=False
    )

    # Save animation to a temporary GIF file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".gif") as tmpfile:
        ani.save(tmpfile.name, writer="pillow")
        gif_path = tmpfile.name

    # Return GIF + message
    if found_index == -1:
        return gif_path, ":( Target not found"
    else:
        return gif_path, f":) Target found at index {found_index}"

# Gradio interface: two outputs (image + text)
demo = gr.Interface(
    fn=visualize_linear_search,
    inputs=["text", "text"],
    outputs=["image", "text"],  # animation + message
    title="Linear Search Visualizer",
    description="Enter numbers (comma-separated) and a target number."
)

demo.launch()
