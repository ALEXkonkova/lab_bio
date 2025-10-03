SUBDIRS := "test/atb" "test/caesar" "test/cwrd" "test/rew" "test/rle" "test/rot1"

test: example_test test_source $(SUBDIRS)

example_test:
	./test_main.py < input_example

$(SUBDIRS):
	$(MAKE) -C $@

test_source:
	if test -f /mnt/smartclass/validator; then \
	CURDIR=`pwd`; \
	/mnt/smartclass/validator coder $$CURDIR; \
	fi

test_atb:
	$(MAKE) -C test/atb test

test_caesar:
	$(MAKE) -C test/caesar test

test_cwrd:
	$(MAKE) -C test/cwrd test

test_rew:
	$(MAKE) -C test/rew test

test_rle:
	$(MAKE) -C test/rle test

test_rot1:
	$(MAKE) -C test/rot1 test