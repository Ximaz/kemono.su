#!/bin/sh

coverage run -m unittest discover --pattern "tests_*.py" --start-directory tests/ >& /dev/null
coverage report -m --omit="tests/tests_*.py,kemono/__init__.py" > coverage.txt
python3 -c ""
echo "::group::Coverage"
while IFS= read -r line; do
    args=($line)
    [[ ! -f "${args[0]}" ]] && continue
    echo "::debug::${args[0]} ${args[3]}"
done < coverage.txt
echo "::endgroup::"

rm -rf coverage.txt
