using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using System.Drawing;
using System.Windows.Forms;
using GTA;

public class GatherData : Script
{
    public GatherData()
    {
        Tick += OnTick;
        KeyUp += OnKeyUp;
        KeyDown += OnKeyDown;
    }

    private void OnTick(object sender, EventArgs e)
    {
    }

    private void OnKeyDown(object sender, KeyEventArgs e)
    {
        Ped playerPed = Game.Player.Character;
        string filepath = "vehicle_data.csv";
        if (playerPed.IsInVehicle() & e.KeyCode == Keys.F5)
        {
            Vehicle vehicle = playerPed.CurrentVehicle;
            string timestamp = DateTime.Now.ToString("hh:mm:ss.fff");

            float Sa = vehicle.SteeringAngle; //float in range [-40.0,40.0]
            float Sp = vehicle.Speed; //float mph speed divided by 2.2
            float Tr = vehicle.Throttle; //float in range [0,1]
            float Br = vehicle.BrakePower; //float in range [0,1]

            try
            {
                using (System.IO.StreamWriter file = new System.IO.StreamWriter(@filepath, true))
                {
                    file.WriteLine(timestamp + "," + Sa.ToString("F3", System.Globalization.CultureInfo.InvariantCulture) + "," + Sp.ToString("F3", System.Globalization.CultureInfo.InvariantCulture) + "," + Tr.ToString("F3", System.Globalization.CultureInfo.InvariantCulture) + "," + Br.ToString("F3", System.Globalization.CultureInfo.InvariantCulture));
                }
            }
            catch (Exception ex)
            {
                throw new ApplicationException("there was exception:", ex);
            }
        }
    }

    private void OnKeyUp(object sender, KeyEventArgs e)
    {
    }
}