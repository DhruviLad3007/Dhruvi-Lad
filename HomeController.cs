using Microsoft.AspNetCore.Mvc;

namespace Ass3_First_ASP_NET_core_App.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
