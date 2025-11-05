"""
Government Shutdown board module implementation.
"""
import logging
from datetime import datetime
from typing import Tuple

from PIL import Image

from boards.base_board import BoardBase
from data.data import Data
from renderer.matrix import Matrix

from . import __board_name__, __description__, __version__

debug = logging.getLogger("scoreboard")

# ---- Helpers -----------------------------------------------------------------

def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

def _calculate_elapsed_time(start_datetime: datetime, current_datetime: datetime) -> Tuple[int, int, int, int]:
    """
    Calculate elapsed time since start and return (days, hours, minutes, seconds).
    """
    time_delta = current_datetime - start_datetime

    days = time_delta.days
    total_seconds = int(time_delta.total_seconds())
    hours = (total_seconds // 3600) % 24
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return days, hours, minutes, seconds


# ---- Main class --------------------------------------------------------------

class GovernmentShutdownBoard(BoardBase):
    """
    The **Government Shutdown Board** displays elapsed time since the government
    shutdown started on October 1, 2025 at 12:01 AM.
    """

    def __init__(self, data: Data, matrix: Matrix, sleepEvent):
        super().__init__(data, matrix, sleepEvent)

        # Board metadata from package
        self.board_name = __board_name__
        self.board_version = __version__
        self.board_description = __description__

        # Get configuration values with defaults
        self.display_seconds = self.board_config.get("display_seconds", 10)
        self.fg_color = self.board_config.get("fg_color", "#FF0000")
        self.title_color = self.board_config.get("title_color", "#FFFFFF")

        # Shutdown start time: October 1, 2025 at 12:01 AM
        self.shutdown_start = datetime(2025, 10, 1, 0, 1, 0)

        # Access standard application config
        self.font = data.config.layout.font
        self.font_large = data.config.layout.font_large

        # Set some additional class properties
        self.rows = self.matrix.height
        self.cols = self.matrix.width

    # -------- Rendering --------

    def render(self):
        debug.info("Rendering Government Shutdown Board")

        self.matrix.clear()

        layout = self.get_board_layout("government_shutdown")

        # Load gradient background
        black_gradient = Image.open(f'assets/images/{self.cols}x{self.rows}_scoreboard_center_gradient.png')

        # Calculate elapsed time
        current_time = datetime.now()
        days, hours, minutes, seconds = _calculate_elapsed_time(self.shutdown_start, current_time)

        # Convert colors to RGB
        fg_rgb = _hex_to_rgb(self.fg_color)
        title_rgb = _hex_to_rgb(self.title_color)

        # Draw gradient background
        self.matrix.draw_image_layout(layout.gradient, black_gradient)

        # Draw title
        self.matrix.draw_text_layout(layout.title_text, "SHUTDOWN", fillColor=title_rgb)

        # Draw elapsed time components
        self.matrix.draw_text_layout(layout.days_value, str(days), fillColor=fg_rgb)
        self.matrix.draw_text_layout(layout.days_label, "DAYS", fillColor=title_rgb)

        self.matrix.draw_text_layout(layout.hours_value, str(hours), fillColor=fg_rgb)
        self.matrix.draw_text_layout(layout.hours_label, "HRS", fillColor=title_rgb)

        self.matrix.draw_text_layout(layout.minutes_value, str(minutes), fillColor=fg_rgb)
        self.matrix.draw_text_layout(layout.minutes_label, "MIN", fillColor=title_rgb)

        self.matrix.draw_text_layout(layout.seconds_value, str(seconds), fillColor=fg_rgb)
        self.matrix.draw_text_layout(layout.seconds_label, "SEC", fillColor=title_rgb)

        # Render to screen
        self.matrix.render()

        # Update every second to keep seconds counter accurate
        self.sleepEvent.wait(1)
