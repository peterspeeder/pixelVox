from settings import *


class ShaderProgram():
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.player = app.player
        # Shaders --
        self.chunk = self.get_program(shader_name='chunk')

        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        self.chunk['m_proj'].write(self.player.m_proj)
        self.chunk['m_model'].write(glm.mat4())
        self.chunk['u_texture_0'] = 0

    def update(self):
        self.chunk['m_view'].write(self.player.m_view)

    def get_program(self, shader_name):
        vertex_shader_path = f'shaders/{shader_name}.vert'
        fragment_shader_path = f'shaders/{shader_name}.frag'

        print(f"Loading vertex shader from: {vertex_shader_path}")
        with open(vertex_shader_path) as file:
            vertex_shader = file.read()

        print(f"Loading fragment shader from: {fragment_shader_path}")
        with open(fragment_shader_path) as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

