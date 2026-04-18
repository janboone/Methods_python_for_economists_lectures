from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MatrixMultiplicationIntro(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))

        title = Text("Matrix–Vector Multiplication", font_size=28)
        with self.voiceover(text="Let's see how matrix vector multiplication works."):
            self.play(Write(title))
            self.wait(1)
        self.remove(title)

        A = Matrix([
            [1, 2, 3],
            [0, 1, 4],
            [2, 0, 1]
        ])

        x = Matrix([
            [11],
            [12],
            [13]
        ])

        matrices = VGroup(A, x).arrange(RIGHT, buff=0.4)
        matrices.scale(0.5)

        with self.voiceover(text="We start with a three by three matrix and a three dimensional vector."):
            self.play(Create(matrices))
            self.wait(1)

        # Highlight column of x
        col_rect = SurroundingRectangle(x.get_columns()[0], color=BLUE)
        with self.voiceover(text="To compute the product, we take a row of the matrix and multiply it with the vector."):
            self.play(Create(col_rect))

        # ----- Row 1 -----
        row_rect = SurroundingRectangle(A.get_rows()[0], color=YELLOW)
        expr1 = MathTex(r"1 \cdot 11 + 2 \cdot 12 + 3 \cdot 13 = 74")
        expr1.scale(0.6)
        expr1.next_to(matrices, DOWN)

        with self.voiceover(text="For the first row we multiply each entry with the corresponding element of the vector and add them up."):
            self.play(Create(row_rect))
            self.play(Write(expr1))
            self.wait(1)

        # ----- Row 2 -----
        row2_rect = SurroundingRectangle(A.get_rows()[1], color=YELLOW)
        expr2 = MathTex(r"0 \cdot 11 + 1 \cdot 12 + 4 \cdot 13 = 64")
        expr2.scale(0.6)
        expr2.next_to(matrices, DOWN)

        with self.voiceover(text="We repeat the same procedure for the second row."):
            self.play(ReplacementTransform(row_rect, row2_rect), ReplacementTransform(expr1, expr2))
            self.wait(1)

        # ----- Row 3 -----
        row3_rect = SurroundingRectangle(A.get_rows()[2], color=YELLOW)
        expr3 = MathTex(r"2 \cdot 11 + 0 \cdot 12 + 1 \cdot 13 = 35")
        expr3.scale(0.6)
        expr3.next_to(matrices, DOWN)

        with self.voiceover(text="And again for the third row."):
            self.play(ReplacementTransform(row2_rect, row3_rect), ReplacementTransform(expr2, expr3))
            self.wait(1)

        # Final result Ax = b
        equals = MathTex("=")
        b = Matrix([
            [74],
            [64],
            [35]
        ])
        b.scale(0.5)

        # Remove explanation but keep matrices, then shift left
        self.play(FadeOut(expr3), FadeOut(row3_rect), FadeOut(col_rect))
        self.play(matrices.animate.shift(LEFT*0.8))

        equals.next_to(x, RIGHT, buff=0.2)
        b.next_to(equals, RIGHT, buff=0.2)

        self.play(Write(equals), Create(b))

        self.wait(2)


class DynamicSystemMatrixForm(Scene):
    def construct(self):
        title = Text("Dynamic System\n as Matrix Multiplication", font_size=28)
        self.play(Write(title))
        self.wait(1)
        self.remove(title)


        # Transition equations
        eq1 = MathTex(r"u_{t+1} = u_t + \delta_l l_t + \delta_h h_t - \mu u_t")
        eq2 = MathTex(r"l_{t+1} = l_t + \mu u_t - \lambda l_t - \delta_l l_t")
        eq3 = MathTex(r"h_{t+1} = h_t + \lambda l_t - \delta_h h_t")

        equations = VGroup(eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        equations.scale(0.6)
        equations.to_edge(LEFT)

        # Arrange equations but do not show them yet
        equations.set_opacity(0)

        # Matrix representation
        A = Matrix([
            ["1-\\mu", "\\delta_l", "\\delta_h"],
            ["\\mu", "1-\\lambda-\\delta_l", "0"],
            ["0", "\\lambda", "1-\\delta_h"]
        ], h_buff=2.0, v_buff=1.0, element_alignment_corner=ORIGIN)

        x = Matrix([
            ["u_t"],
            ["l_t"],
            ["h_t"]
        ])

        y = Matrix([
            ["u_{t+1}"],
            ["l_{t+1}"],
            ["h_{t+1}"]
        ])

        equals = MathTex("=")

        system = VGroup(y, equals, A, x).arrange(buff=0.4)
        system.scale(0.3)
        system.to_edge(LEFT)
        

        self.play(Create(system))
        self.wait(1)

        # Highlight row of A and column of x
        row_box = SurroundingRectangle(A.get_rows()[0], color=YELLOW)
        col_box = SurroundingRectangle(x.get_columns()[0], color=BLUE)
        self.play(Create(row_box), Create(col_box))
        self.wait(1)
        equations.set_opacity(1)
        eq1.next_to(system, DOWN)
        self.play(Write(eq1))
        # Fade out the blue column highlight at the end
        self.play(FadeOut(row_box))
        self.wait(1)
        self.play(FadeOut(eq1))

        # equation 2
        
        row_box = SurroundingRectangle(A.get_rows()[1], color=YELLOW)
        self.play(Create(row_box))
        self.wait(1)
        eq2.next_to(system, DOWN)
        self.play(Write(eq2))
        # Fade out the blue column highlight at the end
        self.play(FadeOut(row_box))
        self.wait(1)
        self.play(FadeOut(eq2))

        # equation 3
        
        row_box = SurroundingRectangle(A.get_rows()[2], color=YELLOW)
        self.play(Create(row_box))
        self.wait(1)
        eq3.next_to(system, DOWN)
        self.play(Write(eq3))
        # Fade out the blue column highlight at the end
        # self.play(FadeOut(row_box))
        self.wait(1)
        self.play(FadeOut(eq3))

        # Fade out matrix system
        self.play(FadeOut(system), FadeOut(row_box), FadeOut(col_box))

        # Show full system of equations
        equations.scale(0.9)
        equations.move_to(UP)
        # equations.move_to(ORIGIN)
        self.play(Write(eq1))
        eq2.next_to(eq1,DOWN)
        self.play(Write(eq2))
        eq3.next_to(eq2,DOWN)
        self.play(Write(eq3))


        self.wait(2)
