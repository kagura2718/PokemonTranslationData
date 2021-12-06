# PokemonTranslationData

## Summary

This repository data come from wiki:

https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7

## License

License under Creative Commons

https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode.txt

This License policy is under:

https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3Wiki:%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3Wiki%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6

## Data

Main data is json that have:

- generatedAt: UTC time with iso format
- version: version string of the data and structure.
- data: Array of translation. Each item have "i18n" and any supplement field.

## Maintenance policy

- Maintener need [json_pp](https://github.com/deftek/json_pp)
- NOTE: Under version "0.x.x" may drastically changed the json field.

### Major version

After release "1.0.0" should not be change major version. 
But following case should upgrade the major number.

- Field is changed.
- Field is removed.

### Minor version

- New Field is added.

### Revision version

- Misunderstanding by wiki editor.
- Some other reason, officially changed.
- This repository parser's bug.
- Any other reason translation data is changed.

# TODO

- glossary.json
  https://wiki.xn--rckteqa2e.com/wiki/%E3%82%AB%E3%83%86%E3%82%B4%E3%83%AA:%E4%B8%80%E8%A6%A7

- type.json
 improve i18n (currently just en, ja)

 