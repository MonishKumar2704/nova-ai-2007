"""YouTube tools.

This module registers all YouTube-related tools with the central
ToolRegistry.

Current tools:
youtube.channel.my_uploads
"""

from future import annotations

from app.integrations.youtube_api import YouTubeApiClient
from app.tools.registry import ToolRegistry

from app.tools.youtube.channel import MyUploadsTool

def register_youtube_tools(
registry: ToolRegistry,
*,
client: YouTubeApiClient,
) -> None:
"""Register all YouTube tools with the central tool registry.

```
Args:
    registry: Central ToolRegistry instance used by the application.
    client: Shared YouTube API client used by YouTube tools.

Returns:
    None
"""

# ------------------------------------------------------------------
# Channel tools
# ------------------------------------------------------------------

# List videos uploaded by the connected Google account's
# own YouTube channel.
registry.register(
    MyUploadsTool(client=client)
)
```
