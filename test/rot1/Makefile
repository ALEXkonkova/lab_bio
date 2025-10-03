test:
	for u in *.conf; \
	do \
	CUR_TES_NAM=`echo $$u | sed -e 's/.conf//g'`; \
	CUR_OUT=`echo $$u | ../../test_main.py`; \
	CUR_INP=`cat "$$CUR_TES_NAM".a`; \
	if test ! "$$CUR_OUT" = "$$CUR_INP" ; then \
	exit 1; \
	fi; \
	done