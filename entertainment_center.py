import media
import fresh_tomatoes

# Creating Movie instances
alaska = media.Movie("Alaska",
                     "https://www.travelalaska.com/~/media/"
                     "Images/TravelAlaska/Content/"
                     "misc/planner2.jpg?h=513&la=en&mw=400&w=400",
                     "https://www.youtube.com/watch?"
                     "v=_iYZx27EtVk&index=10&list="
                     "PLgWdSDe9zj0KaoqwvYn4rQYoUrby-"
                     "iOEZ&pbjreload=10")
russia = media.Movie("Russia",
                     "https://encrypted-tbn0.gstatic.com/"
                     "images?q=tbn:ANd9GcSMm7WoF3NYdv-"
                     "CLnpcrUE0FTtsEDHNLgD_HG785vTHz5SxZ1cEzA",
                     "https://www.youtube.com/"
                     "watch?v=Su9a2soT1O4&list="
                     "PLgWdSDe9zj0KaoqwvYn4rQYoUrby-"
                     "iOEZ&index=9")
yemen = media.Movie("Yemen",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:AN"
                    "d9GcRR2AZZkgZV_wAeqFhQkKzsteIKlOgZlC9I0Qvplg"
                    "fi_bkxgXVurg",
                    "https://www.youtube.com/"
                    "watch?v=27_hdiY9S6E&list=PLgWdSDe9zj0KaoqwvYn4rQYoUrby"
                    "-iOEZ&index=8")
sicily = media.Movie("Sicily",
                     "https://encrypted-tbn0.gstatic.com/"
                     "images?q=tbn:ANd9GcTnIcdf7aDPBMfW0W6t"
                     "s2NUB0CN040woGY2fSAJPMYvuYJPCvcJ",
                     "https://www.youtube.com/watch?"
                     "v=nwwa9tjGU_8&list=PLgWdSDe9zj0Kaoqwv"
                     "Yn4rQYoUrby-iOEZ&index=7")
tajikistan = media.Movie("Tajikistan",
                         "https://encrypted-tbn0.gstatic.com/images?"
                         "q=tbn:ANd9GcQBCp5q0bYyawxh5Wqa2k0g"
                         "V1p6706SP6n6LytCfoxVcob7sHdW",
                         "https://www.youtube.com/watch?"
                         "v=DhUitvCZGFo&index=6&list=PLgW"
                         "dSDe9zj0KaoqwvYn4rQYoUrby-iOEZ")
siberia = media.Movie("Siberia",
                      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS"
                      "ZaJ9j4aWzxqq6vwOz2u8r2DnIaWz2SSd9KIm5-jUbsSAjng5q",
                      "https://www.youtube.com/watch?"
                      "v=3oLeOvVXLvo&list=PLgWdSDe9zj0Ka"
                      "oqwvYn4rQYoUrby-iOEZ&index=3")

# Open the webpage
fresh_tomatoes.open_movies_page(
        [alaska, russia, yemen, sicily, tajikistan, siberia])
