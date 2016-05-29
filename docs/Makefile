# generate html from adoc file(s)
#
# usage:
#    make html

# we need html output, as the chrome adoc renderer does not show include:: contents
html: csp_01_json.html

csp_01_json.html: csp_01_json.adoc
	asciidoctor -v $?

.PHONY: csp_01_json.html
