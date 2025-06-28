import gradio as gr
from agents import evolve_agent
from emotion import get_emotion_level
from shared_memory import MemoryStore

memory = MemoryStore()

def evolve_step(target_value: float, emotion_input: str):
    emotion_mod = get_emotion_level(emotion_input)
    result_a = evolve_agent('Agent A', target_value, emotion_mod, memory)
    result_b = evolve_agent('Agent B', target_value, emotion_mod, memory)
    best = max([result_a, result_b], key=lambda x: x['score'])
    return f"Best result: {best['agent']} => Expression: {best['expression']} (Score: {best['score']})"

demo = gr.Interface(
    fn=evolve_step,
    inputs=[
        gr.Number(label="Target Value"),
        gr.Radio(["Calm", "Frustrated", "Curious"], label="User Emotion")
    ],
    outputs="text",
    title="Multi-Agent Evolution Sandbox",
    description="Two agents evolve Python expressions to match a target number. Emotions influence their exploration."
)

demo.launch()