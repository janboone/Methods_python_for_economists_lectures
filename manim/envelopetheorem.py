from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class EnvelopeTheorem(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))

        title = Text("Envelope Theorem", font_size=28)
        with self.voiceover(text="In this video we explain the envelope theorem."):
            self.play(Write(title))
            self.wait(1)
        self.play(FadeOut(title))

        # Definition
        eq1 = MathTex(r"F(t) = \max_x f(x,t)")
        eq1.scale(0.6)
        # eq1.shift(UP*2)

        with self.voiceover(text="Suppose we define a value function F of t as the maximum of a function f over x."):
            self.play(Write(eq1))
        self.play(FadeOut(eq1))

        eq2 = MathTex(r"\frac{dF(t)}{dt} = \frac{\partial f(x,t)}{\partial t}")
        eq2.scale(0.5)
        eq2.shift(UP*0.9)

        with self.voiceover(text="The envelope theorem tells us that the derivative of this value function with respect to t equals the partial derivative of f with respect to t."):
            self.play(Write(eq2))

        chain = MathTex(r"\frac{dF(t)}{dt} = \frac{\partial f(x,t)}{\partial t} + \frac{\partial f(x,t)}{\partial x} \frac{dx}{dt}")
        chain.scale(0.5)
        chain.next_to(eq2, DOWN * 0.6, buff=0.4)

        with self.voiceover(text="If we differentiate before using optimality, the chain rule gives two terms: the direct effect and the effect through x."):
            self.play(Write(chain))

        eq3 = MathTex(r"\frac{\partial f(x,t)}{\partial x} = 0")
        eq3.scale(0.5)
        eq3.next_to(chain, DOWN * 0.6, buff=0.4)

        with self.voiceover(text="But at the optimum the first order condition implies that the derivative with respect to x is zero."):
            self.play(Write(eq3))

        self.wait(1)

        self.play(FadeOut(eq2), FadeOut(chain), FadeOut(eq3))

        # Example function
        f = MathTex(r"f(x,t) = x^2 - 2tx + 10")
        f.scale(0.5)
        f.shift(UP)

        with self.voiceover(text="Let's look at a concrete example."):
            self.play(Write(f))

        foc = MathTex(r"\frac{\partial f}{\partial x} = 2x - 2t = 0")
        foc.scale(0.5)
        foc.next_to(f, DOWN, buff=0.6)

        with self.voiceover(text="First we compute the first order condition."):
            self.play(Write(foc))

        xstar = MathTex(r"x^*(t) = t")
        xstar.scale(0.5)
        xstar.next_to(foc, DOWN, buff=0.6)

        with self.voiceover(text="Solving this gives the optimal choice x star equal to t."):
            self.play(Write(xstar))

        self.wait(1)
        
        self.play(FadeOut(f), FadeOut(foc), FadeOut(xstar))

        # Substitute into value function
        sub = MathTex(r"F(t) = f(t,t) = t^2 - 2t^2 + 10 = -t^2 + 10")
        sub.scale(0.5)
        sub.shift(UP)

        with self.voiceover(text="Substituting the optimal x into the function gives the value function."):
            self.play(Write(sub))

        deriv = MathTex(r"F'(t) = -2t")
        deriv.scale(0.5)
        deriv.next_to(sub, DOWN, buff=0.6)

        with self.voiceover(text="Taking the derivative with respect to t gives minus two t."):
            self.play(Write(deriv))

        self.wait(1)
        self.play(FadeOut(sub), FadeOut(deriv))

        # Envelope theorem derivative
        ft = MathTex(r"f_t = -2x")
        ft.scale(0.6)
        ft.shift(UP)

        with self.voiceover(text="Now compute the partial derivative of f with respect to t."):
            self.play(Write(ft))

        plug = MathTex(r"f_t(x^*(t),t) = -2t")
        plug.scale(0.6)
        plug.next_to(ft, DOWN, buff=0.6)

        with self.voiceover(text="If we substitute the optimal x equal to t, we obtain minus two t, exactly the same result."):
            self.play(Write(plug))

        self.wait(2)
