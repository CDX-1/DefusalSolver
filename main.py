from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Grid, Horizontal
from textual.screen import Screen
from textual.widgets import Static, Button, TabbedContent, TabPane, SelectionList, Select, Label, MaskedInput, Switch, \
    RadioSet, RadioButton, Footer
import numpy as np
import re

class DefusalSolverApp(App):
    def on_mount(self) -> None:
        self.push_screen(EntryScreen())

class EntryScreen(Screen):
    CSS = """
    EntryScreen {
        align: center middle;
    }

    #frame {
        width: auto;
        height: auto;
        padding: 2 4;
        border: round $primary;
        align: center middle;
    }
    
    #title {
        text-align: center;
        padding-bottom: 1;
    }
    
    #continue {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Defusal Solver", id="title"),
            Button("Continue", variant="primary", id="continue"),
            id="frame"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.push_screen(MainMenuScreen())

class MainMenuScreen(Screen):
    CSS = """
    Tabs {
        dock: top;
    }
    
    TabPane {
        align: center middle;
        padding: 2;
    }
    
    .tab-container {
        border: round $primary;
        text-align: center;
        width: auto;
        height: auto;
        padding: 2 4;
    }
    
    SelectionList {
        padding: 1;
        border: round $primary;
    }
    
    Select {
        padding: 1;
        border: round $primary;
    }
    
    MaskedInput {
        border: round $primary;
    }
    
    #keypads-grid {
        layout: grid;
        grid-size: 2 2;
        height: auto;
    }
    """

    BINDINGS = [
        Binding('ctrl+r', 'reset', 'Reset')
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Home"):
                yield Static("Use the tabs above to select a module to solve", classes="tab-container")

            with TabPane("Wires"):
                # Represents the present wires
                yield SelectionList[int](
                    ("White", 0),
                    ("Red", 1),
                    ("Yellow", 2),
                    ("Green", 3),
                    ("Blue", 4),
                    ("Orange", 5),
                    id="wires-selection"
                )

                yield Static()

                # Represents the active light
                yield Select.from_values([
                    "Red",
                    "Yellow",
                    "Green",
                    "Blue",
                    "White"
                ], prompt="No light", id="wires-light")

                yield Static()

                # The label that shows the answer
                yield Label("There is no solution", id="wires-answer")

            with TabPane("Button"):
                # Represents the button color
                yield Select.from_values([
                    "Blue",
                    "Red",
                    "White",
                    "Grey",
                ], prompt="Select the color", id="button-color")

                yield Static()

                # Represents the button text
                yield Select.from_values([
                    "Detonate",
                    "Abort",
                    "Blank"
                ], prompt="Select the text", id="button-text")

                yield Static()

                # The label that shows the answer
                yield Label("There is no solution", id="button-answer")

            with TabPane("Hexadecimal"):
                # Represents the hexadecimal text
                yield MaskedInput(
                    template="HH-HH-HH-HH;0",
                    id="hexadecimal-enter",
                )

                yield Static()

                # The label that shows the answer
                yield Label("There is no solution", id="hexadecimal-answer")

            with TabPane("Tiles"):
                # Represents the left tile
                yield Select.from_values([
                    "Red",
                    "Green",
                    "Blue",
                    "Yellow",
                    "Pink",
                    "White"
                ], id="tiles-left")

                yield Static()

                # Represents the right tile
                yield Select.from_values([
                    "Red",
                    "Green",
                    "Blue",
                    "Yellow",
                    "Pink",
                    "White"
                ], id="tiles-right")

                yield Static()

                # The label that shows the answer
                yield Label("There is no solution", id="tiles-answer")

            with TabPane("Keypads", id="keypads-tab"):
                with Grid(id="keypads-grid"):
                    yield MaskedInput(
                        template="90;0",
                        id="keypads-1",
                        classes="keypads"
                    )
                    yield MaskedInput(
                        template="90;0",
                        id="keypads-2",
                        classes="keypads"
                    )
                    yield MaskedInput(
                        template="90;0",
                        id="keypads-3",
                        classes="keypads"
                    )
                    yield MaskedInput(
                        template="90;0",
                        id="keypads-4",
                        classes="keypads"
                    )

                yield Static()

                # The label that shows the answer
                yield Label("There is no solution", id="keypads-answer")

            with TabPane("Binary"):
                yield Static("Select the switches that are on")
                yield Static()

                # Represents the switches that are on
                yield Horizontal(
                    Switch(id="binary-1", classes="binary-switch"),
                    Switch(id="binary-2", classes="binary-switch"),
                    Switch(id="binary-3", classes="binary-switch"),
                    Switch(id="binary-4", classes="binary-switch"),
                    Switch(id="binary-5", classes="binary-switch"),
                    Switch(id="binary-6", classes="binary-switch"),
                    Switch(id="binary-7", classes="binary-switch")
                )

                # The label that shows the answer
                yield Label("There is no solution", id="binary-answer")

            with TabPane("Mathematics"):
                yield Static("Enter the letters")

                yield Static()

                # Represents the mathematics entry
                yield MaskedInput(template="AA-AA;0", id="mathematics-enter")

                yield Static()

                # The label that shows the answer
                yield Label("There is no solution", id="mathematics-answer")

            with TabPane("Color Code"):
                # Represents the color lines
                with Horizontal(id="color-code-colors", classes="tab-container"):
                    yield RadioSet(
                        "Red",
                        "Green",
                        "Blue",
                        "Yellow",
                        "White",
                        id="color-code-color-1",
                        classes="color-code-colors"
                    )
                    yield RadioSet(
                        "Red",
                        "Green",
                        "Blue",
                        "Yellow",
                        "White",
                        id="color-code-color-2",
                        classes="color-code-colors"
                    )
                    yield RadioSet(
                        "Red",
                        "Green",
                        "Blue",
                        "Yellow",
                        "White",
                        id="color-code-color-3",
                        classes="color-code-colors"
                    )
                    yield RadioSet(
                        "Red",
                        "Green",
                        "Blue",
                        "Yellow",
                        "White",
                        id="color-code-color-4",
                        classes="color-code-colors"
                    )
                    yield RadioSet(
                        "Red",
                        "Green",
                        "Blue",
                        "Yellow",
                        "White",
                        id="color-code-color-5",
                        classes="color-code-colors"
                    )

                yield Static()

                yield Static("Enter the code")

                # Represents the code
                yield MaskedInput(template="AAAAA;0", id="color-code-letters")

                yield Static()

                # The label that shows the answer
                yield Label("There is no solution", id="color-code-answer")

            with TabPane("Multi Button"):
                yield Static("Enter the code")

                # Represents the code
                yield MaskedInput(template="999999;0", id="multi-buttons-code")

                yield Static()

                # The label that shows the answer
                yield Label("There is no solution", id="multi-buttons-answer")

            with TabPane("Timing"):
                yield Static("Enter the code")

                # Represents the code
                yield MaskedInput(template="99-AA;0", id="timing-code")

                yield Static()

                # The label that shows the answer
                yield Label("There is no solution", id="timing-answer")

        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#wires-selection").border_title = "Which of the following wires are present"
        self.query_one("#wires-light").border_title = "Select the color of the light above the wires, if any"

        self.query_one("#button-color").border_title = "Select the color of the button"
        self.query_one("#button-text").border_title = "Select the text on the button"

        self.query_one("#hexadecimal-enter").border_title = "Enter the hexadecimal code"

        self.query_one("#tiles-left").border_title = "Select the color of the left tile"
        self.query_one("#tiles-right").border_title = "Select the color of the right tile"

        self.query_one("#keypads-1").border_title = "Top Left"
        self.query_one("#keypads-2").border_title = "Top Right"
        self.query_one("#keypads-3").border_title = "Bottom Left"
        self.query_one("#keypads-4").border_title = "Bottom Right"

        self.query_one("#color-code-colors").border_title = "Select the colors that appear"

    @on(SelectionList.SelectedChanged)
    def selection_list_changed(self, event: SelectionList.SelectedChanged):
        if event.selection_list.id == "wires-selection":
            self.calculate_wires()

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed):
        if event.select.id == "wires-light":
            self.calculate_wires()
        elif event.select.id in ["button-color", "button-text"]:
            self.calculate_button()
        elif event.select.id in ["tiles-left", "tiles-right"]:
            self.calculate_tiles()

    @on(MaskedInput.Changed)
    def masked_input_changed(self, event: MaskedInput.Changed):
        if event.input.id == "hexadecimal-enter":
            self.calculate_hexadecimal()
        elif "keypads" in event.input.classes:
            self.calculate_keypads()
        elif event.input.id == "mathematics-enter":
            self.calculate_mathematics()
        elif event.input.id == "color-code-letters":
            self.calculate_color_code()
        elif event.input.id == "multi-buttons-code":
            self.calculate_multi_buttons()
        elif event.input.id == "timing-code":
            self.calculate_timing()

    @on(Switch.Changed)
    def switch_changed(self, event: Switch.Changed):
        if "binary-switch" in event.switch.classes:
            self.calculate_binary()

    @on(RadioSet.Changed)
    def radio_set_changed(self, event: RadioSet.Changed):
        if "color-code-colors" in event.radio_set.classes:
            self.calculate_color_code()

    """ON THE SUBJECT OF THE WIRES"""
    def calculate_wires(self):
        active_wires: list[str] = self.query_one("#wires-selection").selected
        wire_count: int = len(active_wires)
        light: str | None = self.query_one("#wires-light").selection

        def update(answer: int | None = None):
            if answer:
                self.query_one("#wires-answer").update(f"Cut the {answer} wire")
            else:
                self.query_one("#wires-answer").update("There is no solution")

        if wire_count == 3:
            if "Red" not in active_wires:
                update(1)
            elif "White" in active_wires:
                update(2)
            elif "Blue" in active_wires:
                update(3)
        elif wire_count == 4:
            if "Green" not in active_wires:
                update(1)
            elif "Blue" not in active_wires:
                update(2)
            elif "White" not in active_wires:
                update(3)
            else:
                update(4)
        elif wire_count == 5 and light is not None:
            if light == "Red":
                update(1)
            elif light == "Green":
                update(2)
            elif light == "Blue":
                update(3)
            elif light == "Yellow":
                update(4)
            else:
                update(5)
        else:
            update()

    """ON THE SUBJECT OF THE BUTTON"""
    def calculate_button(self):
        button_color: str = self.query_one("#button-color").selection
        button_text: str = self.query_one("#button-text").selection

        def update(clicks: int | None = None):
            if clicks is None:
                self.query_one("#button-answer").update("There is no solution")
            else:
                if clicks <= 2:
                    direction = "down"
                else:
                    direction = "up"
                self.query_one("#button-answer").update(f"Click the button {clicks} time(s) and then click {direction}")

        if button_color == "Blue" and button_text == "Detonate":
            update(1)
        elif button_color == "Red":
            update(2)
        elif button_text == "Abort":
            update(3)
        elif button_color == "White" or button_color == "Grey":
            update(4)
        else:
            update()

    """ON THE SUBJECT OF HEXADECIMAL"""
    def calculate_hexadecimal(self):
        raw: str = self.query_one("#hexadecimal-enter").value
        split = raw.split("-")

        def update(answer: str | None = None):
            if answer is None:
                self.query_one("#hexadecimal-answer").update("There is no solution")
            else:
                self.query_one("#hexadecimal-answer").update(f"Enter '{answer}' then submit")

        try:
            code = ''.join(chr(int(h, 16)) for h in split)
            if len(code) != 4:
                update()
            else:
                update(code)
        except ValueError:
            update()

    """ON THE SUBJECT OF THE TILES"""
    def calculate_tiles(self):
        left: str = self.query_one("#tiles-left").selection
        right: str = self.query_one("#tiles-right").selection

        mapping = {
            'Red': 1,
            'Green': 9,
            'Blue': 7,
            'Yellow': 2,
            'Pink': 6,
            'White': 5
        }

        def update(answer: int | None = None):
            if answer is None:
                self.query_one("#tiles-answer").update("There is no solution")
            else:
                self.query_one("#tiles-answer").update(f"Enter '{answer}' then submit")

        if left is None or right is None:
            update()
            return

        left_value = mapping[left]
        right_value = mapping[right]
        update(left_value + right_value)

    """ON THE SUBJECT OF THE KEYPADS"""
    def calculate_keypads(self):
        def update(ordered: list[str] | None = None):
            if ordered is None:
                self.query_one("#keypads-answer").update("There is no solution")
            else:
                replace_map = {
                    'tl': "Top Left",
                    'tr': "Top Right",
                    'bl': "Bottom Left",
                    'br': "Bottom Right"
                }
                mapped_list = [replace_map.get(val, val) for val in ordered]
                ordered_str = str.join(", ", mapped_list)
                self.query_one("#keypads-answer").update(f"Click the keypads in this order: {ordered_str}")

        try:
            tl: int = int(self.query_one("#keypads-1").value)
            tr: int = int(self.query_one("#keypads-2").value)
            bl: int = int(self.query_one("#keypads-3").value)
            br: int = int(self.query_one("#keypads-4").value)
        except ValueError:
            update()
            return

        if tl < 10:
            x = 15
        elif tl in range(10, 20):
            x = 20
        elif tl in range(20, 80):
            x = 30
        else:
            x = 10

        if tr < 10:
            x += 10
        elif tr in range(10, 20):
            x *= 2
        elif tr in range(20, 80):
            x *= 3
        else:
            x -= 10

        if bl < 10:
            x *= 2
        elif bl in range(10, 20):
            x *= 3
        elif bl in range(20, 80):
            x -= 5

        if br < 10:
            x *= 2
        elif br in range(10, 20):
            x += 20
        elif br in range(20, 80):
            x += 50
        else:
            x *= 3

        y = (tl + tr + bl + br) / 2
        z = x - y

        if z <= 0:
            update(["tl", "tr", "bl", "br"])
        elif z in np.arange(0.5, 19.5):
            update(["tl", "tr", "br", "bl"])
        elif z in np.arange(20, 49.5):
            update(["br", "bl", "tr", "tl"])
        elif z in np.arange(50, 89.5):
            update(["br", "bl", "tr", "tl"])
        elif z >= 90:
            update(["tr", "bl", "tl", "br"])

    """ON THE SUBJECT OF BINARY"""
    def calculate_binary(self):
        switches = []
        for i in range(1, 7 + 1):
            switches.append(self.query_one(f"#binary-{i}").value)

        def update(answer: int):
            self.query_one("#binary-answer").update(f"Click the red button {answer} time(s), then submit")

        if True not in switches:
            update(1)
        elif switches[1] == True and switches[6] == False:
            update(2)
        elif switches[0] == True and switches[1] == True:
            update(3)
        elif switches[0] == False and switches[6] == False:
            update(4)
        elif not False in switches[:4]:
            update(6)
        elif not False in switches[:3]:
            update(5)
        elif switches.count(False) > 3:
            update(7)
        elif False not in switches:
            update(9)
        elif switches.count(True) > 5:
            update(8)
        else:
            update(10)

    """ON THE SUBJECT OF MATHEMATICS"""
    def calculate_mathematics(self):
        raw: str = self.query_one("#mathematics-enter").value

        def update(answer: int | None = None):
            if answer is None:
                self.query_one("#mathematics-answer").update("There is no solution")
            else:
                self.query_one("#mathematics-answer").update(f"Enter '{answer}' then submit")

        if not re.match(r"^[A-J]{2}-[A-J]{2}$", raw):
            update()
            return

        split = raw.split("-")

        mapping = {
            'A': '1',
            'B': '3',
            'C': '7',
            'D': '2',
            'E': '4',
            'F': '5',
            'G': '6',
            'H': '0',
            'I': '8',
            'J': '9'
        }

        left = int(''.join(mapping.get(ch, ch) for ch in split[0]))
        right = int(''.join(mapping.get(ch, ch) for ch in split[1]))
        answer = left * right
        update(answer)

    """ON THE SUBJECT OF COLOR CODE"""
    def calculate_color_code(self):
        colors: list[str] = []
        letters_raw: str = self.query_one("#color-code-letters").value

        invalid_chars = [ch for ch in letters_raw if ch not in ['R', 'G', 'B', 'Y', 'W']]

        def update(answer: str | None = None):
            if answer is not None:
                self.query_one("#color-code-answer").update(f"Click the red button {answer} times, then submit")
            else:
                self.query_one("#color-code-answer").update("There is no solution")

        if invalid_chars or len(letters_raw) != 5:
            update()
            return

        for i in range(1, 5 + 1):
            radio_set: RadioSet = self.query_one(f"#color-code-color-{i}")
            active: RadioButton | None = radio_set.pressed_button

            if not active:
                update()
                return

            colors.append(str(active.label))

        color_mapping = {
            'Red': 0,
            'Green': 0,
            'Blue': 0,
            'Yellow': 0,
            'White': 0
        }

        letter_mapping = {
            'R': 1,
            'G': 3,
            'B': 2,
            'Y': 3,
            'W': 4
        }

        y = sum(list(map(lambda entry: color_mapping[entry], colors)))
        x = sum(list(map(lambda entry: letter_mapping[entry], list(letters_raw))))
        z = x - y

        update(z)

    """ON THE SUBJECT OF MULTI BUTTONS"""
    def calculate_multi_buttons(self):
        raw: str = self.query_one("#multi-buttons-code").value

        def update(answer: list[str] | None = None):
            if answer is None:
                self.query_one("#multi-buttons-answer").update("There is no solution")
            else:
                self.query_one("#multi-buttons-answer").update(f"Click the buttons in this order: {', '.join(answer)}")

        if len(raw) != 6:
            update()
            return

        nums = list(map(lambda e: int(e), list(raw)))
        ordered = []

        if nums[0] < 6:
            ordered.append("Red")
        else:
            ordered.append("Orange")

        if nums[1] < 6:
            ordered.append("Yellow")
        else:
            ordered.append("Green")

        if nums[2] < 6:
            ordered.append("Blue")
        else:
            ordered.append("Purple")

        def add_remaining(order: list[int]):
            chunked = [["Red", "Orange"], ["Yellow", "Green"], ["Blue", "Purple"]]
            for i in order:
                chunk = chunked[i - 1]
                if chunk[0] in ordered:
                    ordered.append(chunk[1])
                else:
                    ordered.append(chunk[0])

        if nums[3] < 7:
            add_remaining([2, 3, 1])
        elif nums[4] < 7:
            add_remaining([3, 2, 1])
        elif nums[5] < 7:
            add_remaining([1, 2, 3])
        else:
            add_remaining([1, 3, 2])

        update(ordered)

    """ON THE SUBJECT OF TIMING"""
    def calculate_timing(self):
        raw: str = self.query_one("#timing-code").value
        split = raw.split("-")

        def update(answer: str | None = None):
            if answer is None:
                self.query_one("#timing-answer").update("There is no solution")
            else:
                self.query_one("#timing-answer").update(f"Click the button when the color is {answer}")

        if len(raw) != 5:
            update()
            return

        invalid_chars = [ch for ch in split[1] if ch not in ['A', 'B', 'C', 'D']]

        if invalid_chars:
            update()
            return

        mapping = {
            'A': 4,
            'B': 3,
            'C': 7,
            'D': 9
        }

        left = int(split[0][0]) + int(split[0][1])
        right = sum(list(map(lambda e: mapping[e], list(split[1]))))
        answer = left * right

        if answer in range(0, 59):
            update("White")
        elif answer in range(60, 99):
            update("Red")
        elif answer in range(100, 199):
            update("Yellow")
        elif answer in range(200, 299):
            update("Green")
        elif answer in range(300, 399):
            update("Blue")
        elif answer in range(400, 499):
            update("Yellow")
        elif answer in range(500, 599):
            update("Red")
        elif answer >= 600:
            update("White")
        else:
            update()

    def action_reset(self):
        self.query_one("#wires-selection").deselect_all()
        self.query_one("#wires-light").clear()

        self.query_one("#button-color").clear()
        self.query_one("#button-text").clear()

        self.query_one("#hexadecimal-enter").clear()

        self.query_one("#tiles-left").clear()
        self.query_one("#tiles-right").clear()

        for i in range(1, 4 + 1):
            self.query_one(f"#keypads-{i}").clear()

        for i in range(1, 7 + 1):
            if self.query_one(f"#binary-{i}").value:
                self.query_one(f"#binary-{i}").toggle()

        self.query_one("#mathematics-enter").clear()

        self.query_one("#color-code-letters").clear()
        self.query_one("#multi-buttons-code").clear()
        self.query_one("#timing-code").clear()

        for module in ["wires", "button", "hexadecimal", "tiles", "keypads", "binary", "mathematics", "color-code", "multi-buttons"]:
            self.query_one(f"#{module}-answer").update("There is no solution")

if __name__ == "__main__":
    app = DefusalSolverApp()
    app.run()