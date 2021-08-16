from datetime import datetime
import sys
if sys.version_info[0] != 3 or sys.version_info[1] < 7:
	print("Plus requires Python version 3.7 or greater")
	sys.exit(1)

# Metadata
name = "Plus"
description = "mangaplus chapter discussion bot"
version = "0.1.0"

import os
from pathlib import Path
os.chdir(str(Path(__file__).parent.parent))

from data import database
import services

def main(config, args, extra_args):
	from logging import debug, info, warning, error, exception
	
	# Set things up
	db = database.initialize_database(config.database)
	if not db:
		error("Cannot continue running without a database")
		return

	# services.setup_services(config) 
	
	# Run the requested module
	try:
		debug("Running module {}".format(config.module))
		if config.module == "setup":
			info("Setting up database")
			db.setup_tables()
		elif config.module=="edit":
			info("Editing database")
			import module_edit as m
			m.main(config,db,*extra_args)
		elif config.module == "chapter":
			info("Finding new chapters")
			import module_find_chapters as m
			m.main(config,db,debug=c.debug)
		elif config.module == "update":
			info("Updating manga")
			import module_update_manga as m
			m.main(config, db,*extra_args)
		else:
			warning("Program broke")
	except:
		exception("Unknown exception or error")
		db.rollback()
	
	db.close()
	
if __name__ == "__main__":
	# Parse args
	import argparse
	parser = argparse.ArgumentParser(description="{}, {}".format(name, description))
	parser.add_argument("--no-input", dest="no_input", action="store_true", help="run without stdin and write to a log file")
	parser.add_argument("-m", "--module", dest="module", nargs=1, choices=["setup", "edit", "chapter", "update"], default=["chapter"], help="runs the specified module")
	parser.add_argument("-c", "--config", dest="config_file", nargs=1, default=["config.ini"], help="use or create the specified database location")
	parser.add_argument("-d", "--database", dest="db_name", nargs=1, default=None, help="use or create the specified database location")
	parser.add_argument("-s", "--subreddit", dest="subreddit", nargs=1, default=None, help="set the subreddit on which to make posts")
	parser.add_argument("-o", "--output", dest="output", nargs=1, default="db", help="set the output mode (db or yaml) if supported")
	parser.add_argument("-L", "--log-dir", dest="log_dir", nargs=1, default=["logs"], help="set the log directory")
	parser.add_argument("-v", "--version", action="version", version="{} v{}, {}".format(name, version, description))
	parser.add_argument("-D","--debug", action="store_true", default=False)
	parser.add_argument("extra", nargs="*")
	args = parser.parse_args()
	
	# Load config file
	import config
	config_file = os.environ["PLUS_CONFIG"] if "PLUS_CONFIG" in os.environ else args.config_file[0]
	c = config.from_file(config_file)
	if c is None:
		print("Cannot start without a valid configuration file")
		sys.exit(2)
	
	# Override config with args
	c.debug |= args.debug
	c.module = args.module[0]
	c.log_dir = args.log_dir[0]
	if args.db_name is not None:
		c.database = args.db_name[0]
	if args.subreddit is not None:
		c.subreddit = args.subreddit[0]
	
	# Start
	use_log = args.no_input
	
	import logging
	from logging.handlers import TimedRotatingFileHandler
	if use_log:
		os.makedirs(c.log_dir, exist_ok=True)
		
		log_file = "{dir}/plus_{mod}.log".format(dir=c.log_dir, mod=c.module)
		logging.basicConfig(
			handlers=[TimedRotatingFileHandler(log_file, when="midnight", backupCount=7, encoding="UTF-8")],
			format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S",
			level=logging.DEBUG if c.debug else logging.INFO)
	else:
		logging.basicConfig(format="%(levelname)s | %(message)s", level=logging.DEBUG if c.debug else logging.INFO)

	logging.getLogger("requests").setLevel(logging.WARNING)
	logging.getLogger("praw-script-oauth").setLevel(logging.WARNING)
	
	from logging import info, warning
	from time import time
	
	if use_log:
		info("------------------------------------------------------------")
	err = config.validate_config(c)
	if err:
		warning("Configuration state invalid: {}".format(err))
	
	if c.debug:
		info("DEBUG MODE ENABLED")
        
	start_time = time()
	main(c, args, args.extra)
	end_time = time()
	
	time_diff = end_time - start_time
	info("")
	info("Run time: {:.6} seconds".format(time_diff))
	
	if use_log:
		info("------------------------------------------------------------\n")

