#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([Akhet], [0.0.1], [BUG-REPORT-ADDRESS])

# Checks for programs.
AC_PROG_AWK
AC_CHECK_PROG(DOCKER, [docker],[docker],[no])
test "x$docker" == "xno" && AC_MSG_ERROR([Required program 'docker' not found.])

#compare versions
function version_gt() { test "$(echo "$@" | tr " " "\n" | sort -V | head -n 1)" != "$1"; }

if version_gt "17.04.0" $(docker --version | cut -d" " -f3 | tr -d ','); then
	AC_MSG_ERROR([docker version must be higher then 17.04.0], [-1])
fi


#help message for user
if ! id -nG "$USER" | grep -qw "docker"; then
	AC_MSG_WARN([The current user is not in docker group])
fi

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
