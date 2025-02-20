# ------------------------------------
# Copyright (c) Microsoft Corporation. All Rights Reserved.
# Licensed under the MIT License.
# See License in the project root for license information.
# ------------------------------------
from typing import Any, Dict, Union

from .request_adapter import RequestAdapter


class BaseRequestBuilder:
    """Base class for all request builders"""

    def __init__(
        self, request_adapter: RequestAdapter, url_template: str,
        path_parameters: Union[Dict[str, Any], str]
    ) -> None:
        """Initializes a new instance of the BaseRequestBuilder class."""
        if path_parameters is None:
            path_parameters = {}
        if request_adapter is None:
            raise TypeError("request_adapter cannot be null.")
        if url_template is None:
            raise TypeError("url_template cannot be null.")  # Empty string is allowed

        # Path parameters for the request
        self.path_parameters: Union[Dict[str, Any], str] = path_parameters
        # Url template to use to build the URL for the current request builder
        self.url_template: str = url_template
        # The request adapter to use to execute the requests.
        self.request_adapter = request_adapter
