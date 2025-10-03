test:
	for u in *.conf; do \
		CUR_TES_NAM=`echo $$u | sed -e 's/.conf//g'`; \
		CUR_OUT=`../../test_main.py <<< "$$u" 2>&1`; \
		CUR_INP=`cat "$$CUR_TES_NAM".a`; \
		\
		if test "$$CUR_OUT" = "ConfigException"; then \
			echo "[$$u] passed (ConfigException)"; \
			continue; \
		fi; \
		if test "$$CUR_OUT" = "$$CUR_INP"; then \
			echo "[$$u] passed"; \
		else \
			echo "[$$u] failed"; \
			exit 1; \
		fi; \
	done
