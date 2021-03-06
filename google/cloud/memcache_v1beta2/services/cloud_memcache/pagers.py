# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Any, Callable, Iterable

from google.cloud.memcache_v1beta2.types import cloud_memcache


class ListInstancesPager:
    """A pager for iterating through ``list_instances`` requests.

    This class thinly wraps an initial
    :class:`~.cloud_memcache.ListInstancesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInstances`` requests and continue to iterate
    through the ``resources`` field on the
    corresponding responses.

    All the usual :class:`~.cloud_memcache.ListInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            [cloud_memcache.ListInstancesRequest], cloud_memcache.ListInstancesResponse
        ],
        request: cloud_memcache.ListInstancesRequest,
        response: cloud_memcache.ListInstancesResponse,
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.cloud_memcache.ListInstancesRequest`):
                The initial request object.
            response (:class:`~.cloud_memcache.ListInstancesResponse`):
                The initial response object.
        """
        self._method = method
        self._request = cloud_memcache.ListInstancesRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[cloud_memcache.ListInstancesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[cloud_memcache.Instance]:
        for page in self.pages:
            yield from page.resources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
