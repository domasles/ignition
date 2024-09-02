#version 460 core

layout (location = 0) out vec4 fragment_color;

void main() {
    vec3 color = vec3(0, 0, 1);
    fragment_color = vec4(color, 1.0);
}
