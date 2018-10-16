using System;
using System.Collections.Generic;
using System.Threading;
using LSL;
using Tobii.Interaction;


namespace ET_EEG_LSL
{
    class Program
    {
        private static Host _host;
        private static GazePointDataStream _gazePointDataStream;
        private List<double> s1 = new List<double>();
        public  double [] sample = new double[3];
     

        private static void InitializeHost()
        {
            _host = new Host();
        }
        private static void DisableConnectionWithTobiiEngine()
        {
            _host.DisableConnection();
        }

        private  void CreateAndVisualizeLightlyFilteredGazePointStream()
        {
            _gazePointDataStream = _host.Streams.CreateGazePointDataStream();
            _gazePointDataStream.GazePoint((x, y, ts) => {
                if (s1.Count == 0)
                {
                    s1.Add(ts);
                }
                sample[0] = ts - s1[0];
                sample[1] = x;
                sample[2] = y;
            }
            );

        }

        static void Main(string[] args)
        {

            // create stream info and outlet
            liblsl.StreamInfo info = new liblsl.StreamInfo("Tobii", "Gaze", 3, 60, liblsl.channel_format_t.cf_double64, "eye_tracker");
            liblsl.StreamOutlet outlet = new liblsl.StreamOutlet(info);
            InitializeHost();
            ConsoleKeyInfo keyinfo;
            //Console.WriteLine(sample.ToString());
            Program p = new Program();
            do
            {
                keyinfo = Console.ReadKey();

                while (!Console.KeyAvailable)
                {
                    p.CreateAndVisualizeLightlyFilteredGazePointStream();
                    //Console.WriteLine(time_st + "  " + eye_x+ "  " + eye_y);
                    //Console.WriteLine(p.sample[0].ToString() + "  " + p.sample[1].ToString() + "  " + p.sample[2].ToString());
                    outlet.push_sample(p.sample);
                    System.Threading.Thread.Sleep(10);
                }

            }
            while (keyinfo.Key != ConsoleKey.Spacebar);
            DisableConnectionWithTobiiEngine();
        }
    }
}