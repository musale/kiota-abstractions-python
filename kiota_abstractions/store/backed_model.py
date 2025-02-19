# ------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation.  All Rights Reserved.
# Licensed under the MIT License.
# See License in the project root for license information.
# ------------------------------------------------------------------------------

from dataclasses import dataclass

from .backing_store import BackingStore


@dataclass
class BackedModel:
    """Defines the contracts for a model that is backed by a store.
    """
    # Stores model information.
    backing_store: BackingStore

    def __post_init__(self):
        self.backing_store.is_initialization_completed = True

    def __setattr__(self, prop, val):
        if prop == "backing_store":
            super().__setattr__(prop, val)
        else:
            self.backing_store.set(prop, val)

    def __getattribute__(self, prop):
        if prop == "backing_store":
            return super().__getattribute__(prop)
        if self.backing_store.get(prop) is not None:
            return self.backing_store.get(prop)
        try:
            attr = super().__getattribute__(prop)
            if callable(attr):  # methods such as serialize and get_field_deserializers
                return attr
            return None
        except AttributeError:
            return None
