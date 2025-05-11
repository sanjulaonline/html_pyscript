from js import document, window, Path2D, Math, requestAnimationFrame
from pyodide.ffi import create_proxy

canvas = document.getElementById("mainCanvas")
ctx = canvas.getContext("2d")

AWS_LOGO_PATH = "M86 66l2 9c0 3 1 5 3 8v2l-1 3-7 4-2 1-3-1-4-5-3-6c-8 9-18 14-29 14-9 0-16-3-20-8-5-4-8-11-8-19s3-15 9-20c6-6 14-8 25-8a79 79 0 0 1 22 3v-7c0-8-2-13-5-16-3-4-8-5-16-5l-11 1a80 80 0 0 0-14 5h-2c-1 0-2-1-2-3v-5l1-3c0-1 1-2 3-2l12-5 16-2c12 0 20 3 26 8 5 6 8 14 8 25v32zM46 82l10-2c4-1 7-4 10-7l3-6 1-9v-4a84 84 0 0 0-19-2c-6 0-11 1-15 4-3 2-4 6-4 11s1 8 3 11c3 2 6 4 11 4zm80 10-4-1-2-3-23-78-1-4 2-2h10l4 1 2 4 17 66 15-66 2-4 4-1h8l4 1 2 4 16 67 17-67 2-4 4-1h9c2 0 3 1 3 2v2l-1 2-24 78-2 4-4 1h-9l-4-1-1-4-16-65-15 64-2 4-4 1h-9zm129 3a66 66 0 0 1-27-6l-3-3-1-2v-5c0-2 1-3 2-3h2l3 1a54 54 0 0 0 23 5c6 0 11-2 14-4 4-2 5-5 5-9l-2-7-10-5-15-5c-7-2-13-6-16-10a24 24 0 0 1 5-34l10-5a44 44 0 0 1 20-2 110 110 0 0 1 12 3l4 2 3 2 1 4v4c0 3-1 4-2 4l-4-2c-6-2-12-3-19-3-6 0-11 0-14 2s-4 5-4 9c0 3 1 5 3 7s5 4 11 6l14 4c7 3 12 6 15 10s5 9 5 14l-3 12-7 8c-3 3-7 5-11 6l-14 2z M274 144A220 220 0 0 1 4 124c-4-3-1-6 2-4a300 300 0 0 0 263 16c5-2 10 4 5 8z M287 128c-4-5-28-3-38-1-4 0-4-3-1-5 19-13 50-9 53-5 4 5-1 36-18 51-3 2-6 1-5-2 5-10 13-33 9-38z"

particles = []
mouse_pos = {"x": 0, "y": 0}
is_touching = False
is_mobile = False
text_image_data = None


def update_canvas_size():
    global is_mobile
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight
    is_mobile = canvas.width < 768


def create_text_image():
    global text_image_data
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    ctx.fillStyle = "white"
    logo_height = 60 if is_mobile else 120
    vercel_width = logo_height * (40 / 19.7762)
    aws_width = logo_height * (283 / 140)
    spacing = 30 if is_mobile else 60
    total_width = vercel_width + aws_width + spacing

    center_x = canvas.width / 2 - total_width / 2
    center_y = canvas.height / 2 - logo_height / 2

    ctx.save()
    ctx.translate(canvas.width / 2, canvas.height / 2)
    aws_scale = logo_height / 140
    ctx.scale(aws_scale, aws_scale)
    ctx.translate(-283 / 2, -70)
    path = Path2D.new(AWS_LOGO_PATH)
    ctx.fill(path)
    ctx.restore()


    text_image_data = ctx.getImageData(0, 0, canvas.width, canvas.height)
    ctx.clearRect(0, 0, canvas.width, canvas.height)


def create_particle():
    for _ in range(100):
        x = Math.floor(Math.random() * canvas.width)
        y = Math.floor(Math.random() * canvas.height)
        idx = (y * canvas.width + x) * 4
        if text_image_data.data[idx + 3] > 128:
            return {
                "x": x,
                "y": y,
                "base_x": x,
                "base_y": y,
                "size": Math.random() * 1 + 0.5,
                "color": "white",
                "scatter": "#FF9900" or "#00DCFF",
                "life": Math.random() * 100 + 50
            }
    return None


def handle_mouse_move(event):
    mouse_pos["x"] = event.clientX
    mouse_pos["y"] = event.clientY


def handle_touch_move(event):
    global is_touching
    if event.touches.length > 0:
        event.preventDefault()
        is_touching = True
        mouse_pos["x"] = event.touches[0].clientX
        mouse_pos["y"] = event.touches[0].clientY


def handle_touch_end(event):
    global is_touching
    is_touching = False
    mouse_pos["x"] = 0
    mouse_pos["y"] = 0


def create_initial_particles(n):
    for _ in range(n):
        p = create_particle()
        if p:
            particles.append(p)


def animate(*args):
    ctx.fillStyle = "black"
    ctx.fillRect(0, 0, canvas.width, canvas.height)

    max_dist = 240
    for p in particles:
        dx = mouse_pos["x"] - p["x"]
        dy = mouse_pos["y"] - p["y"]
        dist = Math.sqrt(dx * dx + dy * dy)

        if dist < max_dist and (is_touching or not hasattr(window, "ontouchstart")):
            force = (max_dist - dist) / max_dist
            angle = Math.atan2(dy, dx)
            p["x"] = p["base_x"] - Math.cos(angle) * force * 60
            p["y"] = p["base_y"] - Math.sin(angle) * force * 60
            ctx.fillStyle = p["scatter"]
        else:
            p["x"] += (p["base_x"] - p["x"]) * 0.1
            p["y"] += (p["base_y"] - p["y"]) * 0.1
            ctx.fillStyle = "white"

        ctx.fillRect(p["x"], p["y"], p["size"], p["size"])

        p["life"] -= 1
        if p["life"] <= 0:
            new_p = create_particle()
            if new_p:
                particles[particles.index(p)] = new_p

    requestAnimationFrame(create_proxy(animate))


def start():
    update_canvas_size()
    create_text_image()
    create_initial_particles(2000)
    animate()


# Event listeners
canvas.addEventListener("mousemove", create_proxy(handle_mouse_move))
canvas.addEventListener("touchmove", create_proxy(handle_touch_move), {"passive": False})
canvas.addEventListener("touchend", create_proxy(handle_touch_end))
window.addEventListener("resize", create_proxy(lambda e: start()))

start()
