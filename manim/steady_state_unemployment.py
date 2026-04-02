from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class DerivationScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        font_size = 20
        # 1. Define Equations
        eq1 = MathTex(r'employed_{t+1} &= employed_{t} + hired_{t} - fired_{t}\\ hired_t &= p_{hired} \cdot unemployed_t \\ fired_t &= p_{fired} \cdot employed_t', font_size=font_size)
        eq2 = MathTex(r"employed_t + unemployed_t = 1", font_size=font_size)
        eq3 = MathTex(
            r"employed &= employed + p_{hired}(1 - employed)\\ &- p_{fired}employed",
            font_size=font_size)
        eq4 = MathTex(
            r"employed = \frac{p_{hired}}{p_{hired} + p_{fired}}",
            font_size=font_size)
        eq5 = MathTex(
            r"unemployed &= 1 - \frac{p_{hired}}{p_{hired} + p_{fired}}\\ &= \frac{p_{fired}}{p_{hired} + p_{fired}}",
            font_size=font_size)
        # 2. Animate
        with self.voiceover(text="We know the following three equations from our model"):
            self.play(Write(eq1))
            self.wait(2)
        # Transform eq1 into eq2 smoothly
        with self.voiceover(text="And we know that people are either employed or unemployed"):
            self.play(ReplacementTransform(eq1, eq2))
            self.wait(1)

        with self.voiceover(text="Combining these equations and noting that in steady state time t does not matter, we can write the following"):
            self.play(ReplacementTransform(eq2, eq3))
            self.wait(1)
        with self.voiceover(text="Finally, we solve this equation for employed which equals"):
            self.play(ReplacementTransform(eq3, eq4))
            self.wait(1)
        with self.voiceover(text="Or equivalently, steady state unemployment equals the following expression"):
            self.play(ReplacementTransform(eq4, eq5))
            self.wait(1)
