import os
import sys
import argparse
import re
import subprocess
import csv
import time

import torch
import esm
import numpy as np

# Import from Python existing libraries
from Bio import SeqIO
from typing import Optional, Dict, List, Tuple, Any
from collections import defaultdict
from pathlib import Path

# Import from user-defined files
from parse_files import parse_args_embed, parse_args_blast
from utils import Hit, filter_hits, write_top_hits, load_model, load_sequences, save_output