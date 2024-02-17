using ChurchMap.Models;
using Microsoft.AspNetCore.Mvc;
using static System.Net.WebRequestMethods;

namespace ChurchMap.Controllers
{
    public class MapController : Controller
    {

        public IActionResult Index(string search = "")
        {
            //tohle všechno si mohu získávat z databáze uložit to do listu a getovat to ale neni čas gg

            if(search == "Čáslav")
            {
                this.ViewBag.Serach = @"https://frame.mapy.cz/s/palufolaka";
                return View(new Search() { Value = search});

            }
            else if(search == "Praha")
            {
                this.ViewBag.Search = @"https://en.frame.mapy.cz/s/jotemacube";
                this.ViewBag.Time = DateTime.Now.Hour.ToString() + ":00";
                this.ViewBag.Priest = "Dmitro Romanovsky";
                this.ViewBag.Color = "#FFFFFF";
                this.ViewBag.Station = "Metro Vyšehrad";
                return View(new Search() { Value = search });

            }
            else if(search == "Plzeň")
            {
                this.ViewBag.Search = "https://en.frame.mapy.cz/s/hukaredaju";
                this.ViewBag.Time = (DateTime.Now.Hour -1).ToString() + ":00";
                this.ViewBag.Priest = "Idk";
                this.ViewBag.Color = "#0000FF";
                this.ViewBag.Station = "Tramvaj u kostela";
                return View(new Search() { Value = search });

            }

            this.ViewBag.Search = @"https://en.frame.mapy.cz/s/nusuvanuku";
            return View(new Search());
        }

        [HttpPost]
        public IActionResult MapFind(Search search)
        {

            return RedirectToAction("Index", new {search = search.Value});
        }
    }
}
