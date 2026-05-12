from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class EulerEquationIntro(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))

        t1 = Text("Dynamic Optimization and", font_size=16)
        t2 = Text("the Euler Equation", font_size=16)
        title = VGroup(t1, t2).arrange(DOWN)

        with self.voiceover(text="In this video we introduce the Euler equation, which is the first order condition for a dynamic optimization problem."):
            self.play(Write(title))

        self.wait(1)
        self.play(FadeOut(title))

        # Recall static optimization
        static_title = Text("Static optimization", font_size=15)

        f = MathTex(r"\max_x f(x)")
        foc = MathTex(r"\frac{df}{dx} = 0")

        group = VGroup(f, foc).arrange(DOWN, buff=0.6)
        group.scale(0.8)

        with self.voiceover(text="You are already familiar with static optimization. We choose a variable x in order to maximize a function f of x."):
            self.play(Write(static_title))

        self.play(FadeOut(static_title))

        with self.voiceover(text="The first order condition says that the derivative of f with respect to x must be equal to zero."):
            self.play(Write(group))

        self.wait(1)
        self.play(FadeOut(group))

        # Introduce dynamic problem
        dyn_title = Text("Dynamic optimization", font_size=15)

        problem = MathTex(r"\max_{x(t)} \int_{t_0}^{t_1} f(t, x(t), x'(t)) \, dt", font_size=20)
        problem.scale(1.0)

        with self.voiceover(text="In dynamic optimization we do not choose a single number. Instead we choose an entire path over time."):
            self.play(Write(dyn_title))

        self.play(FadeOut(dyn_title))

        with self.voiceover(text="The objective function is now an integral over time. The function f depends on time, on the variable x of t, and also on the derivative of x with respect to time."):
            self.play(Write(problem))

        x_path = MathTex(r"x(t) \text{ is a path over time}", font_size=20)
        x_path.next_to(problem, DOWN)

        with self.voiceover(text="So the choice variable is the entire function x of t. You can think of this as choosing a trajectory or path over time."):
            self.play(Write(x_path))

        self.play(FadeOut(problem, x_path))

        # Euler equation
        euler_title = Text("Euler Equation", font_size=20)

        euler = MathTex(
            r"\frac{\partial f}{\partial x} - \frac{d}{dt} \left( \frac{\partial f}{\partial x'} \right) = 0"
        )
        euler.scale(0.5)

        with self.voiceover(text="The first order condition for this dynamic problem is called the Euler equation."):
            self.play(Write(euler_title))

        self.play(FadeOut(euler_title))

        with self.voiceover(text="The Euler equation tells us how the optimal path of x over time must behave."):
            self.play(Write(euler))

        self.wait(1)

        with self.voiceover(text="It balances the direct effect of x on the objective function with the effect of changing the slope of the path."):
            self.wait(1)

        self.play(FadeOut(euler))

        # Intuition section
        intuition_title = Text("Intuition", font_size=20)

        term1 = MathTex(r"\frac{\partial f}{\partial x}")
        term1_text = Text("Direct effect of x", font_size=12)

        term2 = MathTex(r"\frac{\partial f}{\partial x'}")
        term2_text = Text("Effect of changing the slope of x(t)", font_size=12)

        group1 = VGroup(term1, term1_text).arrange(DOWN, buff=0.3)
        group2 = VGroup(term2, term2_text).arrange(DOWN, buff=0.3)

        intuition = VGroup(group1, group2).arrange(RIGHT, buff=2)
        intuition.scale(0.5)

        with self.voiceover(text="To build some intuition, look at the two components that appear in the Euler equation."):
            self.play(Write(intuition_title))

        self.play(FadeOut(intuition_title))

        with self.voiceover(text="The first term is the partial derivative of f with respect to x. This captures the direct effect of changing x at a given moment in time."):
            self.play(Write(group1))

        with self.voiceover(text="The second term involves the partial derivative of f with respect to x prime. This reflects how changing the slope of the path affects the objective over time."):
            self.play(Write(group2))

        self.wait(1)

        # Final slide
        final_eq = MathTex(
            r"\frac{\partial f}{\partial x} - \frac{d}{dt} \left( \frac{\partial f}{\partial x'} \right) = 0"
        )
        final_eq.scale(0.5)

        with self.voiceover(text="At the optimum these effects must balance, which gives the Euler equation."):
            self.play(FadeOut(intuition), Write(final_eq))

        self.wait(2)
