"""YouTube tools.

This module registers all YouTube-related tools with the central
ToolRegistry.

Current tools:
youtube.channel.my_uploads
"""

from __future__ import annotations

from app.integrations.youtube_api import YouTubeApiClient
from app.tools.registry import ToolRegistry

from app.tools.youtube.channel import MyUploadsTool

def register_youtube_tools(registry: ToolRegistry,client: YouTubeApiClient, search_cache:youtube_search_cache) -> None:

# ------------------------------------------------------------------
# Channel tools
# ------------------------------------------------------------------

# List videos uploaded by the connected Google account's
# own YouTube channel.
  registry.register(
      MyUploadsTool(client=client)
  )

