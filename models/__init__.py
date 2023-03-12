#!/usr/bin/python3
"""Initializes the packages"""
import models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
