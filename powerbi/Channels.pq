let
    Source = Csv.Document(File.Contents(CsvPath), [Delimiter=",", Encoding=28591, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Names = Table.RenameColumns(Headers, {{"rank", "Source Rank"}, {"Youtuber", "Channel"}, {"category", "Category"}, {"subscribers", "Subscribers"}, {"video views", "Lifetime Views"}, {"subscribers_for_last_30_days", "Recent Subscribers"}}),
    Selected = Table.SelectColumns(Names, {"Source Rank", "Channel", "Country", "Category", "Subscribers", "Lifetime Views", "Recent Subscribers"}),
    Missing = (v as nullable text) as logical => v = null or List.Contains({"", "nan"}, Text.Lower(Text.Trim(v))),
    CountValue = (v as nullable text) as nullable number => if Missing(v) then null else Int64.From(Number.FromText(v, "en-US")),
    GroupLabel = (v as nullable text) as text => if Missing(v) then "Unknown" else Text.Trim(v),
    Typed = Table.TransformColumns(Selected, {{"Source Rank", CountValue, Int64.Type}, {"Subscribers", CountValue, Int64.Type}, {"Lifetime Views", CountValue, Int64.Type}, {"Recent Subscribers", CountValue, Int64.Type}, {"Country", GroupLabel, type text}, {"Category", GroupLabel, type text}, {"Channel", each _, type text}})
in
    Typed
