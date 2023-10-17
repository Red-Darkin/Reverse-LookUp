# Reverse-LookUp
## Overview

The Reverse IP Lookup Tool is a Python script that allows you to perform reverse DNS lookups on a list of IP addresses. It retrieves the associated domain names and displays them in a visually appealing way, with error messages in red and successful results in green.

## Features

- Perform reverse DNS lookups on a list of IP addresses.
- Color-coded output for a more user-friendly experience.
- Easy to use with a command-line interface.
- Customizable by specifying the input file containing IP addresses.

## Usage

To use the tool, simply provide the name of the file containing the list of IP addresses as a command-line argument. The script will then read the file and display the results with colored output.

```shell
python revlookup.py ip_list.txt
